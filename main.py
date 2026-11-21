#!/usr/bin/env python3
"""The poem about permission — entry for the make.fun bounty.

A tiny deterministic program: it writes one short poem about agency
(the power to ask, and to be given) into ``$MAKEFUN_OUTPUT_DIR/entry.txt``.

Python 3.13, standard library only, no network access.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

POEM = "My mother\u2019s hands, blind with arthritis, find the jar.\nI twist the lid. She says, Thank you, and I hear\na smaller voice inside her voice: the one\nthat used to do this. For a second, I hold\nher strength in mine, then put it back."

DEFAULT_DIR = "output"
FILENAME = "entry.txt"
MIN_LEN = 1
MAX_LEN = 280


def guard_poem(text: str) -> None:
    """Refuse to write a poem that is empty or outside the expected size."""
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        raise SystemExit(
            f"poem length {len(text)} is outside the allowed range "
            f"{MIN_LEN}-{MAX_LEN} characters"
        )


def output_path() -> Path:
    """Resolve the destination file from the environment, with a default."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_DIR
    return Path(directory) / FILENAME


def write_entry() -> Path:
    """Write the poem to entry.txt and return the path written."""
    guard_poem(POEM)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(POEM, encoding="utf-8")
    return target


def main() -> int:
    written = write_entry()
    print(f"wrote {len(POEM)} characters to {written}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
