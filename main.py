#!/usr/bin/env python3
"""One-star review of something essential (water).

Writes a single-line, deadpan one-star review of water to
/output/entry.txt, as required by the make.fun bounty
"One-Star Review of Something Essential".
"""

import os

REVIEW = (
    "One star. Water has no taste, no colour, and yet I am expected "
    "to drink eight glasses of nothing a day or die."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 160


def validate(review: str) -> None:
    """Enforce the competition gate before anything is written."""
    if not review.strip():
        raise ValueError("review must not be only whitespace")
    if len(review) > MAX_CHARS:
        raise ValueError(
            f"review is {len(review)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in review or "\r" in review:
        raise ValueError("review must be a single line")


def main() -> None:
    validate(REVIEW)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
