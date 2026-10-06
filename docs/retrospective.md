# Initialization retrospective

Scope: one central playbook plus one executable business-oriented first project. Public-proxy and production metrics are pending.

What worked: narrow context routes, separate customer/developer execution, zero runtime generative calls, deterministic synthetic smoke and explicit manual data acquisition.

Limits: template scoring depends on alignment; tiny defects may be diluted; no live data/model promotion, real user economics, load testing or production controls. Development token telemetry is unavailable.

v0.2.0 candidates:
- Improve routing using observed context consumption once trustworthy telemetry is available.
- Add a compact cost/evaluation receipt schema if a second project repeats it.
- Record immutable image digests for repeatable containers.
- Add dataset/split receipt validation and a robust comparison baseline after MVTec execution.
- Refine release gates from actual cross-OS CI and operator failure cases.
- Consider runtime package extraction only after repeated reusable implementations, not after this first demo.

These are proposals, not an automatic upgrade. Preserve the current framework gitlink.

