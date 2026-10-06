"""Inventory legally acquired extracted MVTec files; never bypass download forms."""

import argparse
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--data-root", type=Path, required=True)
parser.add_argument("--output", type=Path, default=Path("artifacts/data-manifest.json"))
args = parser.parse_args()
root = args.data_root
files = sorted((root / "bottle").glob("**/*.png"))
if not files or not (root / "bottle" / "train" / "good").is_dir():
    parser.error("Extract the officially acquired dataset so <root>/bottle/train/good exists")
manifest = {
    "dataset": "MVTec AD / bottle",
    "license": "CC-BY-NC-SA-4.0",
    "source": "https://www.mvtec.com/research-teaching/datasets/mvtec-ad",
    "files": [
        {
            "path": p.relative_to(root).as_posix(),
            "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        }
        for p in files
    ],
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
print(f"Inventoried {len(files)} images into {args.output}")
