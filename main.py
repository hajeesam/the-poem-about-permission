#!/usr/bin/env python3
"""The poem about permission — writes the winning poem to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, stdlib only, no network. The poem is 228 characters (1-280 gate).
"""
import os
import sys

POEM = 'My mother’s hands, blind with arthritis, find the jar.\nI twist the lid. She says, Thank you, and I hear\na smaller voice inside her voice: the one\nthat used to do this. For a second, I hold\nher strength in mine, then put it back.'

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)
    return 0

if __name__ == "__main__":
    sys.exit(main())
