#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — make.fun entry.

Writes the graded one-line patch note to entry.txt next to this file.
Pure Python standard library, no network, no input files.

The note: a changelog fix for the brain's nightly rerun of one
embarrassing memory from 2014 at 3 a.m. — a bug every human ships with,
stated in the dry register of a real release note, version number and all.
"""

import os

ENTRY = "v3.9.2: fixed a bug where the brain replayed the same embarrassing memory from 2014 every night at 3 a.m. instead of sleeping."

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    path = os.path.join(HERE, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Grading sandbox: the scorer reads /output/entry.txt, collected as
    # another user, so the copy there must be world-readable (mode 0644).
    out_dir = "/output"
    if os.path.isdir(out_dir):
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(out_path, 0o644)
    print("Wrote %d chars: %r" % (len(ENTRY), ENTRY))


if __name__ == "__main__":
    main()
