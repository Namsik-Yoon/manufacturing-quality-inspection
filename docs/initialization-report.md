# 초기화 완료 보고 — 2026-10-06

Framework와 첫 프로젝트의 코드·문서를 GitHub 공개 저장소에 반영했습니다. 일반 clone과 recursive clone을 실제 원격 저장소에서 검증했고, Windows·macOS·Linux 고객 경로, Docker, 개발자 검증 CI 5개 job이 모두 성공했습니다.

## 1. 생성하거나 수정한 repository

- [solution-delivery-framework](https://github.com/Namsik-Yoon/solution-delivery-framework): 하나의 중앙 framework, 핵심 문서와 템플릿 등 38개 추적 파일.
- [manufacturing-quality-inspection](https://github.com/Namsik-Yoon/manufacturing-quality-inspection): 첫 비즈니스 문제 중심 프로젝트. 코드·문서·환경·lock file·CI·submodule과 이 최종 보고서를 포함합니다.
- Framework [v0.1.0 릴리스](https://github.com/Namsik-Yoon/solution-delivery-framework/releases/tag/v0.1.0) 게시 완료.

## 2. 최종 directory tree

실제 Git 추적 파일 기준입니다. 가상환경, 캐시, Git 내부 파일과 대용량 데이터·실험 산출물은 제외합니다.

```text
solution-delivery-framework/
├── .gitignore
├── AGENTS.md
├── CHANGELOG.md
├── LICENSE
├── README.md
├── VERSION
├── agent/
│   ├── agent-entrypoint.md
│   ├── context-routing.md
│   ├── implementation-instructions.md
│   └── review-instructions.md
├── principles/
│   ├── business-first.md
│   ├── cost-aware-development.md
│   ├── evidence-based-decisions.md
│   └── minimum-viable-delivery.md
├── standards/
│   ├── code-convention.md
│   ├── cost-evaluation.md
│   ├── data-governance.md
│   ├── documentation-convention.md
│   ├── git-convention.md
│   ├── security-and-secrets.md
│   ├── testing-standard.md
│   └── token-accounting.md
├── templates/
│   ├── architecture-decision.md
│   ├── assumption-log.md
│   ├── business-problem.md
│   ├── evaluation-plan.md
│   ├── experiment-report.md
│   ├── retrospective.md
│   ├── runbook.md
│   ├── solution-design.md
│   └── token-report.md
└── workflow/
    ├── implementation.md
    ├── problem-definition.md
    ├── project-lifecycle.md
    ├── release.md
    ├── retrospective.md
    ├── solution-design.md
    └── validation.md

manufacturing-quality-inspection/
├── .devcontainer/
│   ├── Dockerfile
│   └── devcontainer.json
├── .dockerignore
├── .env.example
├── .framework/
│   └── solution-delivery-framework
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── decision.yml
│   │   ├── experiment.yml
│   │   └── task.yml
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── .gitmodules
├── .python-version
├── AGENTS.md
├── Dockerfile
├── LICENSE
├── README.md
├── app/
│   ├── __init__.py
│   └── main.py
├── artifacts/
│   └── README.md
├── data/
│   └── README.md
├── docs/
│   ├── architecture.md
│   ├── assumptions.md
│   ├── baseline-plan.md
│   ├── business-problem.md
│   ├── cost-scenarios.json
│   ├── data-governance.md
│   ├── development-ai-ledger.jsonl
│   ├── evaluation-plan.md
│   ├── experiment-log.md
│   ├── framework-version.json
│   ├── github-workflow.md
│   ├── initialization-report.md
│   ├── project-selection.md
│   ├── retrospective.md
│   ├── runbook.md
│   ├── solution-design.md
│   ├── token-usage.md
│   └── verification.md
├── pyproject.toml
├── scripts/
│   ├── clean_cache.py
│   ├── prepare_data.py
│   ├── verify_environment.py
│   └── verify_framework.py
├── src/
│   └── quality_inspection/
│       ├── __init__.py
│       ├── baseline.py
│       ├── cli.py
│       ├── demo.py
│       └── evaluation.py
├── tests/
│   └── test_workflow.py
└── uv.lock
```

## 3. 주요 설계 결정

중앙 framework 한 개를 개발 전용 submodule로 포함합니다. Runtime, Python import, 패키지 설치, 테스트, Docker, 데이터 pipeline, 고객 문서는 framework를 읽지 않습니다. 고객 CI는 submodule을 초기화하지 않습니다.

AI Agent는 기본 두 문서만 읽고 추가 문서는 작업별로 라우팅합니다. 프로젝트별 명시적 결정이 일반 framework 지침과 충돌하면 이를 기록하고 프로젝트 결정을 따릅니다.

CPU template baseline, FastAPI, 작은 HTML 검토 화면과 batch evaluator를 사용합니다. 정상 후보도 operator 최종 결정을 필요로 하며 자동 제품 출하는 없습니다. Runtime LLM/VLM API 호출은 0회입니다.

## 4. Framework version과 pinned commit

- Version: `v0.1.0`.
- 고정 commit: `2931cbae0b5613426572e1e80563f8bd5b01eca4`.
- 경로: `.framework/solution-delivery-framework`.
- 프로젝트 gitlink, 버전 receipt와 GitHub tag가 같은 commit을 가리킵니다.
- Upgrade는 이전/새 버전과 commit, 이유, 영향, migration, 품질·token 변화를 기록한 명시적 작업으로 수행합니다.

## 5. 첫 프로젝트 선정 이유

제조 품질검사, 설비 고장 경고, 소매 수요 계획을 BU 업무, 데이터 권리·접근성, API/UI 확장, KPI, 비용, 경험 활용과 초기 완성 범위로 비교했습니다.

제조 품질검사는 사용자가 제시한 CV/ML/현장 시스템 경험과 이미지→검토→사람 결정 workflow를 잘 연결합니다. 첫 버전은 bottle 한 종류로 제한했습니다. 비교 근거는 [project-selection.md](project-selection.md)에 있습니다.

[MVTec AD 공식 데이터](https://www.mvtec.com/research-teaching/datasets/mvtec-ad)를 public proxy로 사용합니다. 원본 출처와 사용 조건을 보존하기 위해 mirror 대신 공식 취득 경로를 따릅니다. 데이터는 CC BY-NC-SA 4.0이며 상업적 사용은 허용되지 않습니다. 실제 line의 성능·비용·안전성·사용자 수용성은 아직 검증하지 않았습니다.

## 6. 일반 사용자 실행 방법

Submodule 초기화 없이 실행합니다. Git과 uv 0.12.23이 필요하며, uv가 Python 3.12.15를 준비합니다.

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

http://127.0.0.1:8000 에서 합성 정상/결함 sample과 이미지 upload를 확인합니다. 데이터 다운로드나 API key는 필요 없습니다.

```sh
docker build -t quality-inspection:0.1.0 .
docker run --rm -p 127.0.0.1:8000:8000 quality-inspection:0.1.0
```

## 7. 개발자 및 AI Agent 실행 방법

```sh
git clone --recurse-submodules https://github.com/Namsik-Yoon/manufacturing-quality-inspection.git
cd manufacturing-quality-inspection
uv sync --frozen
uv run python scripts/verify_framework.py
```

기존 clone에서는 `git submodule update --init --recursive`를 사용합니다. Root `AGENTS.md`는 15개 문서를 작업별로 라우팅합니다. Framework 최신 버전을 자동 반영하지 않습니다.

## 8. Codespaces 실행 방법

GitHub에서 Code → Codespaces → Create codespace on main. Devcontainer가 Python 3.12.15, uv 0.12.23, frozen dependency, lint/test, VS Code extension과 환경 검증을 준비합니다.

```sh
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

8000 forwarded port를 private으로 열고, 작업이 끝나면 Codespace를 중지합니다. 실제 사용자 Codespace는 생성하지 않았습니다. 같은 devcontainer 이미지는 로컬 Docker에서 빌드·실행 검증했습니다.

Windows/macOS/Linux의 Local Dev Container는 Docker와 VS Code Dev Containers에서 Reopen in Container로 열 수 있습니다. Host-specific path나 별도 Python 환경은 필요하지 않습니다.

## 9. 수행한 검증과 실제 결과

[상세 검증 기록](verification.md)과 [GitHub CI run 37415675740](https://github.com/Namsik-Yoon/manufacturing-quality-inspection/actions/runs/37415675740)에 근거합니다. 이 CI가 검증한 초기 게시 commit은 `a4bb01c406d609576c5d86bdb2e27640968a19e6`입니다.

- 실제 GitHub 일반 clone: frozen install, Ruff lint/format, Python import/environment, 9 tests, CLI demo 성공. Submodule을 초기화하지 않았습니다.
- 실제 GitHub recursive clone: 고정 framework commit, 버전 receipt와 15 routing file 검증 성공. Local URL 치환 없이 실행했습니다.
- CI: customer ubuntu-latest, customer windows-latest, customer macos-latest, docker, developer의 5개 job 모두 success.
- 로컬 `docker build -t mqi-init:0.1.0 .`와 `docker run --rm mqi-init:0.1.0 python -m quality_inspection.cli demo` 성공.
- Devcontainer `docker build -f .devcontainer/Dockerfile -t mqi-dev:0.1.0 .` 성공. Linux에서 frozen install/environment/9 tests/demo 성공.
- Browser defect sample: `review`, `synthetic-demo`, operator 경고 확인. 정상 score 0.00496687, defect score 0.02321168, threshold 0.00499725. 이는 합성 실행 검증이며 실제 benchmark accuracy가 아닙니다.
- `uv lock --check`, `git diff --check`, host-specific path 검색과 tracked data/weight/secret-pattern inventory 통과.

알려진 warning: 최신 Starlette TestClient의 httpx deprecation 경고가 있지만 테스트는 성공했습니다. Linux read-only 검증 mount의 pytest cache 경고는 실제 쓰기 가능한 Dev Container 환경과 다릅니다.

## 10. 아직 구현하지 않았거나 검증하지 않은 항목

MVTec 공식 form 취득과 실제 baseline 평가, 실제 Codespaces 생성, 현업 사용자·경제성·load/drift 검증은 미실행입니다. Live camera/PLC integration, DB/queue, 공개 인증/TLS/rate limit과 real-model promotion은 v0.1.0 범위 밖입니다.

공식 데이터를 취득하면 아래 명령으로 첫 baseline을 실행할 수 있습니다.

```sh
uv run python scripts/prepare_data.py --data-root data/raw/mvtec-ad
uv run python -m quality_inspection.cli evaluate --data-root data/raw/mvtec-ad --output artifacts/baseline-report.json
```

Label 체계, 모바일 Issue Template과 선택적 GitHub Project board 설정 방법은 문서화했습니다.

Runtime LLM/VLM 호출 및 token API 비용은 0입니다. CPU/hosting/human review 비용은 별도이며 가격은 미측정입니다. 개발 token/tool count/과금 telemetry는 노출되지 않아 unavailable/null로 기록했습니다. Secret, raw data, model weights와 생성된 대용량 산출물은 Git에 넣지 않았습니다.

## 11. Framework v0.2.0 개선 후보

실제 benchmark failure cases에 기반한 평가 receipt 강화, trustworthy telemetry 이후 context 효율 분석, immutable container digest, 반복되는 cost/evaluation schema 재사용과 실제 운영 피드백으로 release gate 개선을 검토합니다. 실행 package 분리는 여러 프로젝트에서 충분한 반복이 확인된 뒤 고려합니다. 현재 프로젝트 pin은 자동 변경하지 않습니다.

