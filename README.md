# Manufacturing Quality Inspection

An executable quality-triage portfolio for a manufacturing quality team: image → anomaly score → review recommendation → operator decision.

**v0.1.0 is a synthetic workflow demo.** The shipped template baseline learns only original procedural images. It is not trained on MVTec, does not certify defects, and never automatically releases products. A separate command evaluates the same baseline on legally acquired MVTec AD bottle data.

Runtime LLM/VLM calls and token API cost: **0**. CPU, hosting and human review still have costs; see [cost and token report](docs/token-usage.md). Development AI telemetry is unavailable, not zero.

## Customer / Reviewer Quick Start

Requires Git and [uv 0.12.23](https://github.com/astral-sh/uv/releases/tag/0.12.23), or use the container/browser path below. uv downloads the pinned Python 3.12.15 when needed.

```sh
git clone https://github.com/Namsik-Yoon/manufacturing-quality-inspection.git
cd manufacturing-quality-inspection
uv sync --frozen
uv run pytest
uv run ruff check .
uv run python scripts/verify_environment.py
uv run python -m quality_inspection.cli demo
uv run python -m app.main
```

Open http://127.0.0.1:8000. Try healthy/defect samples or upload PNG/JPEG (5 MiB, 16 million pixels maximum). Images remain in memory; no credentials or dataset downloads are needed. API: `GET /health`, `POST /inspect`, `GET /samples/healthy`, `GET /samples/defect`; OpenAPI at `/docs`.

These commands work without initializing any submodule.

### Docker

```sh
docker build -t quality-inspection:0.1.0 .
docker run --rm -p 127.0.0.1:8000:8000 quality-inspection:0.1.0
```

Docker exposes the service only on host loopback with the command above. A public deployment needs additional operational controls listed in the [runbook](docs/runbook.md).

## Developer / AI Agent Setup

```sh
git clone --recurse-submodules https://github.com/Namsik-Yoon/manufacturing-quality-inspection.git
cd manufacturing-quality-inspection
uv sync --frozen
uv run python scripts/verify_framework.py
```

For an existing clone: `git submodule update --init --recursive`. The framework is pinned at v0.1.0; see [commit receipt](docs/framework-version.json). `AGENTS.md` routes task-specific reads. Framework upgrades require an explicit architecture decision; runtime never accesses it.

## GitHub Codespaces / Local Dev Container

On GitHub select **Code → Codespaces → Create codespace on main**. The checked-in devcontainer pins Python and uv, installs frozen dependencies plus lint/tests, and runs environment verification automatically. Then run:

```sh
uv run python -m app.main
```

Use the forwarded port 8000. For access through a container port, run `uv run uvicorn app.main:app --host 0.0.0.0 --port 8000`. Keep Codespaces forwarded-port visibility private. Stop the Codespace when finished; account quota/billing is separate from this project's zero runtime LLM cost.

For local Windows/macOS/Linux install Docker and VS Code Dev Containers, clone, and select **Dev Containers: Reopen in Container**. No host-specific paths or preinstalled Python environments are required. Containers use the same devcontainer configuration. The CI customer path also tests all three host OS families.

## Public-data baseline

1. Acquire and extract the official MVTec AD bottle dataset following [rights and manual steps](docs/data-governance.md).
2. Run `uv run python scripts/prepare_data.py --data-root data/raw/mvtec-ad`.
3. Run `uv run python -m quality_inspection.cli evaluate --data-root data/raw/mvtec-ad --output artifacts/baseline-report.json`.

The evaluator reserves every fifth sorted healthy training image for calibration, fits on the rest and uses the untouched official test folders. It reports defect recall, review rate, error-cost scenarios, latency and file hashes. No benchmark performance is claimed before executing this path.

## Delivery evidence

- [Initialization report and final directory tree](docs/initialization-report.md), [executed verification](docs/verification.md)
- [Business problem](docs/business-problem.md), [assumptions](docs/assumptions.md), [candidate selection](docs/project-selection.md)
- [Design](docs/solution-design.md), [architecture and decisions](docs/architecture.md)
- [Evaluation plan](docs/evaluation-plan.md), [baseline plan](docs/baseline-plan.md), [experiment log](docs/experiment-log.md)
- [Runbook](docs/runbook.md), [mobile work and labels](docs/github-workflow.md), [retrospective](docs/retrospective.md)

MIT covers original code/docs. MVTec data is separately CC BY-NC-SA 4.0 and is not distributed here. See [data governance](docs/data-governance.md).
