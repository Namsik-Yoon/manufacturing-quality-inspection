# First project selection — 2026-10-06

Selection is an architecture judgment (**Assumed**); dataset properties below are **Observed** from official publisher pages. No leaderboard score is used.

## 1. manufacturing-quality-inspection — selected

- Business Unit fit: quality engineers reviewing line-camera images; a clear image → triage → human decision workflow.
- Data access/rights: [MVTec AD](https://www.mvtec.com/research-teaching/datasets/mvtec-ad), 15 categories, more than 5,000 images, healthy training and labeled test defects. Official download currently uses a form; CC BY-NC-SA 4.0 restricts commercial use.
- Delivery extension: image API, operator UI, CPU batch evaluation, failure behavior.
- KPI: missed-defect cost, review workload, latency and recoverability.
- Cost/token opportunity: no runtime generative API required; compare local rules/template/small ML before adding costly models.
- Experience fit: strongest use of stated CV/ML and field-system background.
- First-version size: one bottle category, no GPU training, a deterministic offline demo. Real-data evaluation waits for manual lawful acquisition.

## 2. equipment-failure-early-warning

- Business Unit fit: maintenance planning / alarm triage.
- Data access/rights: [UCI AI4I 2020](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset), 10,000 synthetic rows, CC BY 4.0, accessible download.
- Delivery extension: batch risk queues and sensor-input API.
- KPI: false alarms, missed failures, review time. Actual warning lead time cannot be established from same-row failure labels.
- Cost/token opportunity: compact tabular rules/ML and no runtime LLM.
- Experience fit: field/ML experience fits; uses less CV.
- First-version size: lowest ingestion effort, but credible early-warning validation would need longitudinal real equipment data. Do not market same-row classification as predictive lead time.

## 3. retail-demand-planning

- Business Unit fit: inventory planners / daily replenishment.
- Data access/rights: [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii), two years of transactions, CC BY 4.0, accessible download.
- Delivery extension: daily batch forecast and planner UI.
- KPI: demand error and planner workload; stockout/holding-cost claims require unavailable inventory and lead-time assumptions.
- Cost/token opportunity: seasonal baseline, batching and optional explanation templates.
- Experience fit: general ML/delivery fits, weak CV connection.
- First-version size: manageable, but returns/cancellations, missing values and business inventory assumptions widen initial scope.

## Decision

Choose manufacturing-quality-inspection because it combines the stated experience with an observable operator workflow and a bounded one-category baseline. Use the original publisher rather than a Kaggle mirror to preserve provenance and license clarity. The portfolio is noncommercial; commercial deployment requires separately licensed data and real operating validation. This restriction is recorded rather than silently changing it.

All three candidate business cases are hypothetical. The user's stated experience is task context, not independently audited employment evidence.

