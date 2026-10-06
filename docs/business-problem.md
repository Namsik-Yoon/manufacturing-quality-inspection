# Business problem

## Business Unit, user and workflow

**Assumed:** A manufacturing quality team checks bottle images from a fixed line camera. The quality operator reviews each item, marks suspicious cases and asks an engineer to investigate recurring defects. The line supervisor monitors review queue and missed defects.

**Assumed:** Manual review is repetitive, slow and inconsistent when throughput rises. Existing bottlenecks are operator time and queue delay. No measured factory cost or actual customer interview exists.

## Decision and first release

**Assumed:** Help the operator decide which images deserve priority review. Image → local baseline score → `review` or `candidate-pass` → operator decision. v0.1.0 demonstrates this decision support; every product remains human-approved.

**To Validate:** Camera alignment, illumination, defect taxonomy, integration point, operator workflow and acceptable missed-defect risk with a real quality team.

## KPIs and error consequences

**Assumed targets, not achieved:** public-proxy defect recall ≥95%, review rate ≤30% only if the recall constraint holds; p95 inference ≤200 ms on a named CPU under sequential single-image load; 0 automatic product release in the demo; invalid inputs return a clear error and can be retried.

**Assumed cost scenario:** one missed defect = 100 units, one unnecessary review disruption = 1 unit, any human review = 0.5 unit. These are illustrative weights, not currency-valued measured losses. False negatives may send defective products downstream; false positives use operator capacity. Queue volume and final review reliability remain unvalidated.

Measure defect recall, FP/FN counts, candidate-pass/review rates, processing latency, 1,000-image infrastructure/error/review costs, monthly volume scenarios and recovery behavior. Baseline targets may fail; record them honestly.

## Constraints and deployment

**Assumed:** CPU-only local workstation or small container; no GPU, public network API or company data required. PNG/JPEG ≤5 MiB and ≤16 million pixels. No images persist in the API. No live PLC/camera integration, authentication or production HA in v0.1.0.

## Public proxy and limits

**Observed:** [MVTec AD](https://www.mvtec.com/research-teaching/datasets/mvtec-ad) provides industrial object/texture anomaly images, healthy training data and annotated test defects under CC BY-NC-SA 4.0. Scope to bottle only.

**Assumed:** This approximates visual defect triage. It cannot establish the real line's prevalence, economics, human accuracy, lighting drift, safety, throughput, camera alignment, ERP/PLC integration or commercial suitability.

**Observed:** The shipped demo uses original procedural images. Its healthy/defect outputs validate wiring only; no real-data accuracy or business savings have been measured.

