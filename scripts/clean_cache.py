"""Remove only generated local caches, with explicit opt-in."""

import argparse
import shutil
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--confirm", action="store_true")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
targets = [root / ".pytest_cache", root / ".ruff_cache"]
for target in targets:
    print(("Removing " if args.confirm else "Would remove ") + target.name)
    if args.confirm and target.is_dir() and not target.is_symlink():
        shutil.rmtree(target)
print("Raw data and experiment artifacts are preserved.")
