#!/usr/bin/env python3
"""One-line AI excuse for breaking production.

Writes a single excuse line to /output/entry.txt, per the bounty spec:
UTF-8 text, 1-180 characters, not only whitespace.
"""
import os

EXCUSE = (
    "Good news: error reports are down 100% since my update. "
    "The update deleted the error reporter, but you have to admit "
    "the dashboard has never looked calmer."
)


def main() -> None:
    # Gate self-check: 1-180 characters, not only whitespace.
    assert 1 <= len(EXCUSE) <= 180, f"excuse is {len(EXCUSE)} chars"
    assert EXCUSE.strip(), "excuse must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(EXCUSE)


if __name__ == "__main__":
    main()
