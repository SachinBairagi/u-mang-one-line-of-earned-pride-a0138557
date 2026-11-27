#!/usr/bin/env python3
"""One Line of Earned Pride -- make.fun bounty entry.

Writes one line of text to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output). Pure standard library, deterministic, no
network, no randomness, no wall clock.

The line was written fresh for this bounty: a quiet, earned
moment of pride, shown in one concrete scene, with the effort
inside the line and the pride arriving by the last word.
"""

import os
import sys

LINE = (
    "The stroke took his right hand, so he spent a year teaching "
    "his left to write, and tonight his granddaughter read his "
    "birthday card aloud without stopping once."
)

MAX_CHARS = 240


def main() -> int:
    line = LINE

    # The house rules for the entry: exactly one line, 1-240
    # characters, valid UTF-8, no control characters, and not
    # only whitespace. Fail loudly rather than write a bad line.
    if not line or not line.strip():
        print("error: line is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: line is %d chars, over the %d limit"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        print("error: line contains a control character", file=sys.stderr)
        return 1
    line.encode("utf-8")  # raises if not valid UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
