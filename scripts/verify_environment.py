"""Customer check: no submodule reads or host-specific assumptions."""

import platform
import sys
from importlib.metadata import version

EXPECTED_PYTHON = "3.12.15"
assert platform.python_version() == EXPECTED_PYTHON, (
    f"Use Python {EXPECTED_PYTHON}, got {platform.python_version()}"
)
for package in ("fastapi", "numpy", "pillow", "uvicorn"):
    print(f"{package}={version(package)}")
import app.main  # noqa: E402
from quality_inspection.demo import demo_results  # noqa: E402

assert app.main.health()["status"] == "ok"
assert demo_results()["results"][1]["decision"] == "review"
print(f"Environment verified: Python {platform.python_version()} on {sys.platform}")
