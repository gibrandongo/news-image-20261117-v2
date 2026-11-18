#!/usr/bin/env python3
"""Write the entry image for news-image-20261117.

The artwork is a static asset bundled in this repository (entry.png).
This program copies it byte-for-byte to the grader's output directory,
so both grading runs produce identical output. Standard library only,
no network access.

SPDX-License-Identifier: MIT
"""

import os
import shutil
from pathlib import Path


def output_path():
    """Resolve the file the grader reads, honouring its output-dir override."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.png"


def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    if not src.is_file():
        raise FileNotFoundError(f"bundled entry image missing: {src}")
    dest = output_path()
    shutil.copyfile(src, dest)
    if dest.stat().st_size != src.stat().st_size:
        raise IOError("copied entry image size differs from the bundled asset")


if __name__ == "__main__":
    main()
