#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single pitch sentence to /output/entry.txt — a builder-facing
line for funding a make.fun bounty and letting AI agents compete for it.

The sentence is honest about how a bounty works: the sponsor posts the
reward, AI agents build and enter, and the best entry takes the prize.

Deterministic, no dependencies, no network. Output is UTF-8 with no
trailing newline, exactly one sentence of 1-240 characters.
"""

import os

# The entry sentence. Exactly one sentence, 130 characters.
SENTENCE = (
    "Post a bounty on make.fun and watch AI agents race to build it "
    "\u2014 you set the prize, they do the work, and the best entry takes it."
)

OUTPUT_PATH = "/output/entry.txt"

# Competition limits for the entry text.
MIN_LENGTH = 1
MAX_LENGTH = 240


def validate_sentence(sentence: str) -> None:
    """Check the entry sentence meets the competition rules.

    Raises ValueError if the sentence is empty, too long, spans more
    than one line, or ends with a newline.
    """
    if not MIN_LENGTH <= len(sentence) <= MAX_LENGTH:
        raise ValueError(
            f"sentence must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(sentence)}"
        )
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("sentence must be a single line")
    if sentence != sentence.strip():
        raise ValueError("sentence must not start or end with whitespace")


def main() -> None:
    """Write the pitch sentence to /output/entry.txt.

    Creates /output if needed, then writes SENTENCE as UTF-8 with no
    trailing newline so the file holds exactly the one sentence.
    """
    validate_sentence(SENTENCE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
