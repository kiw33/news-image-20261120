#!/usr/bin/env python3
"""Entrypoint for the news-image-20261120 entry.

The image is drawn by draw_news20.py and shipped in this repository
as entry.png. This program only copies it to the output directory, so
both grader runs write exactly the same bytes. Standard library only.
"""

import os
import shutil
import sys


def output_dir():
    """Where the grader wants the image: MAKEFUN_OUTPUT_DIR, else /output.

    Falls back to a local ``out`` directory when neither is set, so the
    entry can also be run by hand without the grader's environment.
    """
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    return "/output"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    dst = os.path.join(out, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
