# Architecture decisions

## ADR-001 — framework boundary — accepted, 2026-10-06

One versioned central repository at `.framework/solution-delivery-framework`, pinned as a Git gitlink. Only developer instructions reference it. Application import, uv install, Docker context, tests, preprocessing, demo and customer docs remain project-owned.

Customer CI deliberately omits submodule checkout; developer CI recursively checks the exact receipt and AGENTS routes. The Docker context excludes `.framework`. No playbook/template/toolkit repos or runtime framework package.

## ADR-002 — local baseline and human decision — accepted

Use NumPy/Pillow template scoring, FastAPI, a small native HTML page and a CLI. No runtime generative service. This minimizes operating tokens and makes failure behavior inspectable. All business performance is pending; demo outputs explicitly identify synthetic evidence.

The live API uses synthetic training/calibration only. Real-data benchmark execution does not promote a model into service. No `pickle`/joblib weight loading.

## ADR-003 — reproducible environments — accepted

Python 3.12.15 and uv 0.12.23; package/transitive versions and hashes in `uv.lock`. Devcontainer and Docker use exact version tags; CI third-party actions use commit SHAs. Image tags pin versions, not immutable digests; digest recording is a follow-up reproducibility improvement.

Codespaces and local Dev Containers share configuration with no host-specific mounts. Direct uv commands work without Make. CI covers Windows/macOS/Linux; local validation scope is recorded in experiment log.

## ADR-004 — evidence and data rights — accepted

MVTec AD bottle is a public proxy with noncommercial data rights. No data redistribution, form bypass or commercial claim. Original synthetic fixtures support offline customer smoke. UCI alternatives and license evidence are recorded in project selection.

## Framework upgrades

Current: v0.1.0, exact commit in `framework-version.json`. Upgrade explicitly with old/new version and commit, reason, project impact, migration and measured/unavailable quality/token difference. Do not run automatic `git submodule update --remote`.

No project/framework conflict exceptions exist in v0.1.0.

