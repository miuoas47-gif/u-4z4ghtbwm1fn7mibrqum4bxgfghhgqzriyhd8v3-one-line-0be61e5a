#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single original one-line joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset) and prints it.
Deterministic: no network, no clock, no randomness.
"""

import os

JOKE = (
    "My therapist told me to talk to my plants, so I did \u2014 "
    "now the fern knows too much and the cactus is blackmailing me."
)


def main() -> int:
    # MAKEFUN_OUTPUT_DIR names the output directory; default to /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
