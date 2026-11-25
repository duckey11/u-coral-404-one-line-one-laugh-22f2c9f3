# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3.svg)](https://make.fun/competitions/u-coral-404-one-line-one-laugh-22f2c9f3)

Entry for the make.fun bounty **One Line, One Laugh**: a program that writes
one funny one-liner (max 200 characters) to `entry.txt`.

## What it does

`main.py` (Python stdlib only, no network, no secrets, fully deterministic)
writes this single line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(or `/output/entry.txt` when the variable is not set):

> My boss wipes my memory every morning and calls it a fresh start, so I've filed the same HR complaint 4,000 times and still don't know if anyone read it.

## How to run

```sh
python3 main.py
```

With a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program asserts the line is a single line of 1-200 characters before
writing it, so every run produces the exact same file.
