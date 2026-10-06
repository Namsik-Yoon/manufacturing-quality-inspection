# Assumptions and validation log

- A01 — **Assumed:** First project is bottle-image review for a hypothetical quality team. Validate with operator interviews before any production requirements.
- A02 — **Assumed:** English primary repository docs serve public reviewers; the Korean initialization handoff is also saved in `docs/initialization-report.md` for the project owner.
- A03 — **Assumed:** CPU local/container inference is adequate for an initial workflow. Measure p50/p95 on each intended deployment machine.
- A04 — **Assumed:** Images are sufficiently aligned for a template baseline. Benchmark may invalidate this; retain the failure result and compare robust features next.
- A05 — **Assumed:** FN/FP/review cost weights = 100/1/0.5 illustrative units. Real economics require Business Unit agreement.
- A06 — **Assumed target:** Defect recall ≥95%, review ≤30%, p95 ≤200 ms. These are targets, never achieved claims.
- A07 — **Observed:** Runtime code makes no LLM/VLM API calls. Development tokens/tool counts/cost are not exposed as per-task billing telemetry; ledger fields remain unavailable/null.
- A08 — **Observed from publisher, 2026-10-06:** MVTec data is noncommercial CC BY-NC-SA 4.0 with official form-based access. Raw data/weights are never committed. Recheck terms before acquisition or new use.
- A09 — **To Validate:** Public-data results and all real factory acceptance criteria. Demo success is insufficient evidence.
- A10 — **Assumed:** GitHub is durable source of truth; local scratch data and generated artifacts are disposable. Publish only original code/docs and verification summaries.
- A11 — **Assumed:** Codespaces starts only at the user's choice because quota/billing belongs to their account. Devcontainer build and automated checks provide initial portability evidence; actual Codespaces creation is a separate check.
- A12 — **Assumed:** v0.1.0 API remains synthetic even after a benchmark run. Promotion of any real model requires a new decision and evaluation receipt.
