#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry (program/v1).

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt:
the single word our grandma would text about AI.

The word is "robit": grandma's spelling of "robot". She has never
typed the word "robot" correctly in her life, and she never will —
but she means it warmly, and she means the machine that talks back.
"""

import os
import sys

WORD = "robit"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.umask(0o022)
    os.makedirs(out_dir, exist_ok=True)
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass
    path = os.path.join(out_dir, "entry.txt")
    data = WORD.encode("utf-8")
    # Gate: 1-30 UTF-8 characters, not only whitespace, and exactly
    # ONE word — no spaces or any whitespace inside the word.
    if not 1 <= len(WORD) <= 30 or not WORD.strip() or len(WORD.split()) != 1:
        sys.exit("entry word fails the one-word gate")
    with open(path, "wb") as fh:
        fh.write(data)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
