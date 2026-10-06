"""Developer-only gitlink, version and AGENTS routing verification."""

import json
import re
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
framework = root / ".framework" / "solution-delivery-framework"
receipt = json.loads((root / "docs" / "framework-version.json").read_text())
actual = subprocess.check_output(
    ["git", "-C", str(framework), "rev-parse", "HEAD"], text=True
).strip()
entry = subprocess.check_output(
    ["git", "-C", str(root), "ls-tree", "HEAD", ".framework/solution-delivery-framework"],
    text=True,
).split()
assert entry[:2] == ["160000", "commit"], "Framework must be a committed gitlink"
assert actual == entry[2] == receipt["commit"], "Framework commit receipt mismatch"
assert (framework / "VERSION").read_text().strip() == receipt["version"]
routes = re.findall(
    r"`((?:agent|principles|standards|workflow|templates)/[^\`]+\.md)`",
    (root / "AGENTS.md").read_text(),
)
assert routes, "No routes found"
for route in routes:
    assert (framework / route).is_file(), f"Missing route: {route}"
print(f"Framework {receipt['version']} @ {actual}: {len(routes)} routes verified")
