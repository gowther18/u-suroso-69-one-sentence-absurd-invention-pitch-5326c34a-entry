#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — make.fun entry.

Writes one absurd invention pitch (122 characters, one sentence) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The pitch is fixed and deterministic: every run writes the exact same
bytes, with no trailing newline, so the two grading runs agree.
"""

import os
import sys

PITCH = (
    "A jar lid that only loosens the moment you hand it to someone "
    "stronger, so you can keep taking full credit for opening it."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
