# Evaluation plan

## Independent evidence tracks

Synthetic smoke: deterministic train seeds 0–29, calibration 100–119, test samples 900/901. Confirms healthy vs marked fixture, API wiring and invalid input behavior only.

Public proxy: MVTec AD bottle healthy fit/calibration split as documented, untouched official test folders. Commands in `baseline-plan.md`. Record Python/dependencies, commit, hardware, hashes and the threshold receipt. First baseline must be run without test tuning. Later comparisons use the same fixed split.

## Model and workflow measures

- Defect recall, TP/TN/FP/FN, review fraction and candidate-pass fraction.
- Automatic-release fraction is always zero in v0.1.0; candidate-pass is a recommendation, not release.
- Sequential per-image p50/p95 including image decode/score on a named machine. API load/concurrency latency is a separate future measurement.
- Error plus review cost per 1,000 = (FN×100 + FP×1 + reviewed×0.5)/n×1,000, with illustrative units explicitly labeled.
- Runtime token API cost is zero; include assumed hosting and human review in cost reports.

**Assumed acceptance targets:** recall ≥95%, review ≤30% only subject to recall, p95 ≤200 ms on specified CPU. The benchmark's class mixture is not the factory prevalence; a review percentage here is not a production queue forecast.

## Failure cases and gates

Test corrupt input, invalid base64, byte/pixel limits, missing fit/calibration and missing dataset layout. Analyze pose/lighting, tiny defects, textured regions and unusual formats.

If recall fails, keep the failed baseline and require review for all items; do not loosen recall goals silently to lower queue volume. Freeze any new calibration procedure before test evaluation.

Production validation requires real line data, prevalence, operator acceptance, error economics, deployment/load/drift and operational controls. None is established by v0.1.0.

