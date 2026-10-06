# Runbook

Install: `uv sync --frozen`. Verify: `uv run python scripts/verify_environment.py`.
Start: `uv run python -m app.main`, local http://127.0.0.1:8000.
Health: open `/health`; expect status ok and model_source synthetic-demo.
Demo: `uv run python -m quality_inspection.cli demo`.
All customer commands work without a submodule.

Configuration: export `MQI_HOST`/`MQI_PORT` or pass uvicorn arguments. `.env.example` is a reference; the app does not automatically load `.env`. No API keys needed.

Normal action: choose demo sample or PNG/JPEG, inspect recommendation/score/source, then decide manually. The service never records a product disposition or releases a product.

Invalid/corrupt/unsupported image: API 422; oversized body: 413. Reduce file size or use valid PNG/JPEG and retry. Model unavailable/service failure: use human inspection, fix/restart service and verify health plus synthetic smoke. Restart reconstructs the deterministic model; no uploads need recovery because none persist.

Logs: uvicorn logs request metadata only; never add raw images/base64/secrets. No retention store exists. API processing is per request, no queue/HA/retries/cache. Benchmark reports stay in ignored artifacts until summarized.

Data preparation and cleanup: follow `data-governance.md`. Never extract untrusted archives in application code. Cache cleaner only handles lint/test caches with explicit confirmation.

Rollback: run a verified prior Git tag with its own lock file and image version; re-run customer smoke. Do not move framework pins automatically.

Deployment boundary: local portfolio demo. Before public/industrial exposure add TLS, authentication/authorization, ingress/rate/body limits, bounded concurrency, monitoring, approved retention, threat review, workload/latency validation and real operator sign-off. The current synthetic API cannot control a production line.

