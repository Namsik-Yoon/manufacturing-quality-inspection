import base64

import pytest
from fastapi.testclient import TestClient

from app.main import MAX_REQUEST_BYTES, app
from quality_inspection.baseline import TemplateBaseline, preprocess
from quality_inspection.cli import benchmark
from quality_inspection.demo import demo_model, synthetic_image
from quality_inspection.evaluation import evaluate

client = TestClient(app)


def test_synthetic_decision_and_preprocessing():
    model = demo_model()
    healthy = synthetic_image(900)
    assert preprocess(healthy).shape == (64, 64)
    assert model.inspect(healthy).decision == "candidate-pass"
    assert model.inspect(synthetic_image(901, True)).decision == "review"


def test_invalid_image_and_missing_calibration():
    with pytest.raises(ValueError):
        preprocess(b"not an image")
    with pytest.raises(ValueError):
        TemplateBaseline.fit([synthetic_image(1)], [], "test")


def test_api_preserves_evidence_and_operator_boundary():
    sample = client.get("/samples/defect").json()
    result = client.post("/inspect", json=sample)
    assert result.status_code == 200
    assert result.json()["decision"] == "review"
    assert result.json()["model_source"] == "synthetic-demo"
    assert result.json()["runtime_llm_tokens"] == 0
    assert "Operator review" in result.json()["warning"]
    assert client.get("/health").json()["status"] == "ok"


@pytest.mark.parametrize("encoded", ["not-base64!", base64.b64encode(b"bad-image").decode()])
def test_invalid_api_input(encoded):
    assert client.post("/inspect", json={"image_base64": encoded}).status_code == 422


def test_stream_limit_without_content_length():
    response = client.post(
        "/inspect",
        content=iter([b"x" * (MAX_REQUEST_BYTES + 1)]),
        headers={"content-type": "application/json"},
    )
    assert response.status_code == 413


def test_business_cost_counts_false_negatives_and_reviews():
    report = evaluate(
        demo_model(),
        [
            (synthetic_image(900), True),  # deliberately wrong label: one FN
            (synthetic_image(901, True), False),  # one FP and review
        ],
    )
    assert (report["fn"], report["fp"]) == (1, 1)
    assert report["scenario_cost_per_1000"] == 50_750
    assert report["automatic_release_rate"] == 0


def test_empty_evaluation_and_invalid_cost():
    with pytest.raises(ValueError):
        evaluate(demo_model(), [])
    with pytest.raises(ValueError):
        evaluate(demo_model(), [(synthetic_image(1), False)], review_cost=float("nan"))


def test_benchmark_uses_healthy_calibration_and_hashes(tmp_path):
    normal = tmp_path / "bottle" / "train" / "good"
    normal.mkdir(parents=True)
    for i in range(15):
        (normal / f"{i:03d}.png").write_bytes(synthetic_image(i))
    for label, defective in (("good", False), ("broken_large", True)):
        directory = tmp_path / "bottle" / "test" / label
        directory.mkdir(parents=True)
        (directory / "test.png").write_bytes(synthetic_image(900, defective))
    report = benchmark(tmp_path)
    assert report["split"] == {"training": 12, "calibration": 3}
    assert report["n"] == 2
    assert len(report["manifest"]) == 17
    assert all(len(item["sha256"]) == 64 for item in report["manifest"])
