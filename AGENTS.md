# AI Agent entrypoint

Framework: `.framework/solution-delivery-framework` (pinned Git submodule).
Read only the documents needed for the current task. Project-specific guidance lives in `docs/`.
Customer install, import, tests, demo, pipelines, Docker and deployment must work without the submodule.

- Every task: `agent/agent-entrypoint.md`, `principles/business-first.md`.
- Code: `standards/code-convention.md`, `agent/implementation-instructions.md`.
- Tests/evaluation: `standards/testing-standard.md`, `workflow/validation.md`.
- LLM/VLM/API cost or development telemetry: `standards/token-accounting.md`, `standards/cost-evaluation.md`.
- Docs: `standards/documentation-convention.md`.
- Data: `standards/data-governance.md`.
- Inputs/secrets/deployment: `standards/security-and-secrets.md`.
- Release: `workflow/release.md`.
- Review: `agent/review-instructions.md`.
- Retrospective: `workflow/retrospective.md`, `templates/retrospective.md`.

Paths above are relative to the framework. Read relevant project decisions in `docs/architecture.md`,
business assumptions and evaluation plan. An explicitly recorded project decision overrides conflicting
general guidance; record the conflict. Do not add runtime dependencies on `.framework`.
Missing framework does not block customer execution; initialize the pinned submodule for agent guidance.
Do not read unrelated documents. Preserve synthetic-vs-benchmark evidence labels and never invent token metrics.

