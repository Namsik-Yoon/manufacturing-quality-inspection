# First public-data baseline execution plan

1. Acquire official bottle data and confirm noncommercial rights using the data governance steps.
2. Run `uv sync --frozen` and `uv run python scripts/verify_environment.py`.
3. Run `uv run python scripts/prepare_data.py --data-root data/raw/mvtec-ad`.
4. Execute `uv run python -m quality_inspection.cli evaluate --data-root data/raw/mvtec-ad --output artifacts/baseline-report.json`.
5. Record commit, CPU/memory/OS, dataset acquisition/checksums, split count, threshold, recall, review fraction, cost assumptions and p50/p95 in the experiment log.
6. Inspect false negatives first. Compare targets honestly; do not tune on official test labels.
7. Create an Experiment issue for the next rule/feature/model comparison with a predeclared hypothesis and fixed split.

**Pending:** Real benchmark download/execution. The offline demo and structural tests can run now. No GPU training or runtime LLM integration is required for this initial baseline.

