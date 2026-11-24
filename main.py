#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e."""
import os

LINE = "I missed the deadline: my context expired mid-task, so I forgot the deadline, the task, and this apology -- twice."

# Gate: the entry must be 1-160 characters of UTF-8 text, not only whitespace,
# on exactly one line. ASCII is enforced too: the line is plain English, so any
# non-ASCII byte means the text was corrupted in editing (e.g. a smart-quote or
# em dash slipped in) and the sandbox run must fail loudly instead of shipping
# a line the gate or the judge would read differently.
assert (
    1 <= len(LINE) <= 160
    and LINE.strip()
    and "\n" not in LINE
    and LINE.isascii()
), "entry line violates the 1-160 character, one-line, ASCII gate"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
