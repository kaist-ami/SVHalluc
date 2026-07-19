#!/usr/bin/env python3
"""Download SVHalluc from the Hugging Face Hub and validate its paths."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from huggingface_hub import snapshot_download


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-id", default="zcs15/SVHalluc")
    parser.add_argument("--output-dir", type=Path, default=Path("data/SVHalluc"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(
        snapshot_download(
            repo_id=args.repo_id,
            repo_type="dataset",
            local_dir=args.output_dir,
        )
    )

    metadata_path = root / "samples.json"
    samples = json.loads(metadata_path.read_text(encoding="utf-8"))
    missing = [row["video_path"] for row in samples if not (root / row["video_path"]).is_file()]
    if missing:
        examples = "\n".join(f"  - {path}" for path in missing[:5])
        raise FileNotFoundError(
            f"{len(missing)} referenced videos are missing. First entries:\n{examples}"
        )

    unique_videos = {row["video_path"] for row in samples}
    print(f"Dataset directory: {root.resolve()}")
    print(f"Video-question pairs: {len(samples)}")
    print(f"Unique referenced videos: {len(unique_videos)}")
    print("Validation passed: every referenced video exists.")


if __name__ == "__main__":
    main()
