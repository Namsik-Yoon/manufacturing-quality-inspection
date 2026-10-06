"""Untouched test evaluation and business-cost scenario accounting."""

import time

import numpy as np

from quality_inspection.baseline import TemplateBaseline


def evaluate(
    model: TemplateBaseline,
    samples: list[tuple[bytes, bool]],
    false_negative_cost: float = 100.0,
    false_positive_cost: float = 1.0,
    review_cost: float = 0.5,
) -> dict:
    if not samples or any(
        not np.isfinite(x) or x < 0 for x in (false_negative_cost, false_positive_cost, review_cost)
    ):
        raise ValueError("Nonempty samples and finite nonnegative costs are required")
    tp = tn = fp = fn = 0
    latency: list[float] = []
    for raw, defective in samples:
        start = time.perf_counter()
        reviewed = model.inspect(raw).decision == "review"
        latency.append((time.perf_counter() - start) * 1000)
        if defective and reviewed:
            tp += 1
        elif defective:
            fn += 1
        elif reviewed:
            fp += 1
        else:
            tn += 1
    count = len(samples)
    scenario_cost = fn * false_negative_cost + fp * false_positive_cost + (tp + fp) * review_cost
    return {
        "model_source": model.source,
        "threshold": model.threshold,
        "preprocessing": "EXIF orientation, grayscale, 64x64 bilinear resize, float32/255",
        "n": count,
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "defect_recall": tp / (tp + fn) if tp + fn else None,
        "review_rate": (tp + fp) / count,
        "candidate_pass_rate": (tn + fn) / count,
        "automatic_release_rate": 0.0,
        "p50_ms": float(np.percentile(latency, 50)),
        "p95_ms": float(np.percentile(latency, 95)),
        "scenario_cost_per_1000": scenario_cost / count * 1000,
        "cost_unit": "assumed currency units; not observed business savings",
        "cost_assumptions": {
            "false_negative": false_negative_cost,
            "false_positive_disruption": false_positive_cost,
            "human_review": review_cost,
        },
        "runtime_llm_tokens": 0,
    }
