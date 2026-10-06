# Initialization verification — 2026-10-06

## Executed before publication

On macOS ARM64, Python 3.12.15 / uv 0.12.23:

- `uv sync --frozen`: passed from a fresh ordinary clone; no submodule initialized.
- `uv run ruff check .`: passed.
- `uv run ruff format --check .`: passed.
- `uv run pytest -q`: 9 passed; one upstream TestClient httpx deprecation warning.
- `uv run python scripts/verify_environment.py`: passed, dependency versions printed.
- `uv run python -m quality_inspection.cli demo`: healthy candidate-pass, defect review. Scores 0.00496687 / 0.02321168 against threshold 0.00499725.
- `uv run python scripts/verify_framework.py`: passed in a recursive local clone, 15 routed files and the committed gitlink verified. The pre-publication clone temporarily redirected the canonical framework URL to the local framework; remote clone checks are recorded below after publication.
- `git diff --check`: passed. Tracked data/weight/secret-pattern inventory contained only `.env.example`, no images, archives, weights or real `.env`.

Docker on Linux ARM64 (Docker Desktop engine 29.4.3):

- `docker build -t mqi-init:0.1.0 .`: passed; framework excluded from context.
- `docker run --rm mqi-init:0.1.0 python -m quality_inspection.cli demo`: passed.
- Container HTTP `/health`: 200, status ok, source synthetic-demo.
- Browser defect sample through the running container: decision review, source synthetic-demo, operator warning visible.
- `docker build -f .devcontainer/Dockerfile -t mqi-dev:0.1.0 .`: passed.
- In the development image, mounted ordinary clone without framework: frozen sync, environment check, 9 tests and CLI demo passed. A pytest cache warning came from the deliberately read-only verification mount; writable Dev Containers do not use that mount.

The sandboxed test host required workspace-local uv/buildx caches. Those paths are verification setup only and do not appear in committed runtime/config files.

## Configured or pending

GitHub CI defines ordinary-clone Windows/macOS/Linux jobs, Docker smoke and recursive developer-pin checks. Remote results are recorded after the initial push.

Actual user-created Codespaces session, MVTec form acquisition and benchmark execution, production workload/latency, real operator acceptance, economics and commercial dataset rights remain unverified. No production KPI is claimed.
