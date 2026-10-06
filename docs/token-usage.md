# Development tokens and runtime cost

## Development AI

Per-task token/tool/billing telemetry is not exposed in this session. The example entry in `development-ai-ledger.jsonl` uses **unavailable** and null for missing measurements. It is not an API bill. Do not infer exact cost from subscription limits or assistant text length.

Future ledger records timestamp/task/stage/model, input/cache/output/reasoning or other billable units, tool calls, artifact/accepted status, retries/rework, price date/source and measured/estimated classification. Cached input is a subset of input; reasoning must not be billed twice if already included in output.

Quality checks accompany tokens per accepted output, cost per completed task, first-attempt success, discarded output ratio and human rework. This initialization has no trustworthy denominator for token-efficiency comparison.

## Runtime

**Observed from source:** no LLM/VLM client or network inference call. Input/output tokens per request = 0; token API cost per request/per 1,000/month = 0. No recurring AI call is necessary for template scoring.

Inference latency, review rate and errors come from the evaluation report; API load p50/p95, retry/failure rate and cache hit rate are **To Validate** under an actual workload. No request cache or automatic retry exists, so no cache benefit is claimed. Invalid requests fail explicitly; the operator can retry. A failed/unvalidated detector falls back to human inspection.

## Infrastructure and review scenarios

`cost-scenarios.json` records illustrative monthly volumes (10k/100k/1M), 160 assumed active CPU hours and unknown dated hourly pricing. Monthly infrastructure is `active_hours × hourly_price + storage + egress`; per-1,000 compute allocation is `monthly_compute / monthly_volume × 1,000`. CPU inference work may scale with volume and concurrency; fixed 160 hours is a scenario, not measured capacity.

Human review cost is `volume × measured_review_rate × agreed_review_unit_cost`. Dataset error-cost weights are illustrative and distinct from hosting spend. Prices, hardware, currency and benchmark capacity remain unknown. Codespaces/Docker-host cost belongs to the chosen account/machine; zero token cost does not mean free operation.

Improvements: compare robust rules and compact local ML, batch inference, avoid redundant decodes, cache only repeated immutable content where retention is approved, and measure operator capacity before making cost-saving claims.

