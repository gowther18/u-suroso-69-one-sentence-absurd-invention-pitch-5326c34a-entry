#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — make.fun entry.

Writes one absurd invention pitch (122 characters, one sentence) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The pitch is fixed and deterministic: every run writes the exact same
bytes, with no trailing newline, so the two grading runs agree.

Before writing, main() validates the pitch against the competition's
entry contract (one sentence, 1-220 chars, no trailing newline) and
fails loudly instead of writing an invalid entry.
"""

import os
import sys

PITCH = (
    "A jar lid that only loosens the moment you hand it to someone "
    "stronger, so you can keep taking full credit for opening it."
)

# Entry contract from the competition rules: one sentence, 1-220 chars.
MIN_CHARS = 1
MAX_CHARS = 220


def validate_pitch(pitch: str) -> None:
    """Raise SystemExit unless pitch satisfies the one-sentence contract."""
    if not (MIN_CHARS <= len(pitch) <= MAX_CHARS):
        raise SystemExit(
            f"pitch must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(pitch)}"
        )
    if pitch != pitch.strip() or "\n" in pitch or "\r" in pitch:
        raise SystemExit("pitch must be a single line with no trailing newline")
    if pitch.count(".") != 1 or not pitch.endswith("."):
        raise SystemExit("pitch must be exactly one sentence ending in one period")


def main() -> int:
    validate_pitch(PITCH)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
