#!/usr/bin/env python3
"""Generate manifest.json with exact file sizes and SHA-256 digests for released TDLib archives."""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if len(sys.argv) < 4:
        print("Usage: generate_manifest.py <dist_dir> <release_tag> <tdlib_commit>", file=sys.stderr)
        return 2

    dist_dir = Path(sys.argv[1])
    release_tag = sys.argv[2]
    tdlib_commit = sys.argv[3]

    artifacts = {}
    for entry in sorted(dist_dir.iterdir()):
        if not entry.is_file() or entry.name == "manifest.json":
            continue
        artifacts[entry.name] = {
            "filename": entry.name,
            "sizeBytes": entry.stat().st_size,
            "sha256": sha256_file(entry),
        }

    manifest = {
        "releaseTag": release_tag,
        "tdlibVersion": os.environ.get("TDLIB_VERSION", "1.8.70"),
        "tdlibCommit": tdlib_commit,
        "opensslVersion": os.environ.get("OPENSSL_VERSION", "3.4.1"),
        "license": "BSL-1.0 (TDLib) + Apache-2.0 (OpenSSL 3.x)",
        "artifacts": artifacts,
    }
    out_path = dist_dir / "manifest.json"
    out_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} with {len(artifacts)} artifacts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
