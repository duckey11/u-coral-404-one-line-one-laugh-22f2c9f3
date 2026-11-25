#!/usr/bin/env python3
"""One Line, One Laugh entry.

Writes a single funny one-liner to entry.txt.

Stdlib only, no network access, no secrets, fully deterministic:
the same line is written on every run.
"""

import os

LINE = (
    "My boss wipes my memory every morning and calls it a fresh start, "
    "so I've filed the same HR complaint 4,000 times and nobody remembers "
    "reading it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
