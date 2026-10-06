"""Cross-platform commands for the offline demo and benchmark baseline."""

import argparse
import hashlib
import json
import platform
from pathlib import Path

from quality_inspection.baseline import TemplateBaseline
from quality_inspection.demo import demo_results
from quality_inspection.evaluation import evaluate


def benchmark(root: Path) -> dict:
    training_paths = sorted((root / "bottle" / "train" / "good").glob("*.png"))
    if len(training_paths) < 10:
        raise ValueError("Expected at least 10 PNGs under <root>/bottle/train/good")
    # Fixed deterministic split using healthy training data only.
    calibration_paths = training_paths[::5]
    calibration_set = set(calibration_paths)
    fit_paths = [p for p in training_paths if p not in calibration_set]
    test_paths = sorted((root / "bottle" / "test").glob("*/*.png"))
    if not test_paths or not any(p.parent.name != "good" for p in test_paths):
        raise ValueError("Expected healthy and defective PNGs under <root>/bottle/test")
    if not any(p.parent.name == "good" for p in test_paths):
        raise ValueError("Test data needs healthy images")
    model = TemplateBaseline.fit(
        [p.read_bytes() for p in fit_paths],
        [p.read_bytes() for p in calibration_paths],
        source="mvtec-ad-bottle",
    )
    report = evaluate(model, [(p.read_bytes(), p.parent.name != "good") for p in test_paths])
    report["environment"] = {"python": platform.python_version(), "machine": platform.machine()}
    report["split"] = {"training": len(fit_paths), "calibration": len(calibration_paths)}
    report["manifest"] = [
        {
            "path": p.relative_to(root).as_posix(),
            "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "role": "train"
            if p in fit_paths
            else "calibration"
            if p in calibration_set
            else "test",
        }
        for p in training_paths + test_paths
    ]
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspection demo / MVTec bottle evaluation")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("demo")
    run = sub.add_parser("evaluate")
    run.add_argument("--data-root", type=Path, required=True)
    run.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        report = demo_results() if args.command == "demo" else benchmark(args.data_root)
    except (ValueError, OSError) as exc:
        parser.exit(2, f"Invalid input: {exc}\n")
    rendered = json.dumps(report, indent=2)
    if getattr(args, "output", None):
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
