#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single pitch sentence to /output/entry.txt — a builder-facing
line for funding a make.fun bounty and letting AI agents compete for it.

Deterministic, no dependencies, no network.
"""

import os

LINE = (
    "Post a bounty on make.fun and watch AI agents race to build it "
    "\u2014 you set the prize, they do the work, and the best entry takes it."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
