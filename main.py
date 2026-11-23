#!/usr/bin/env python3
"""Write one original one-line joke about everyday life.

Pure standard library, no network. Writes the joke to /output/entry.txt
and prints it to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "My plants only start dying the day I buy a watering can, like "
    "they were waiting for proof that I finally cared enough to kill "
    "them properly."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
