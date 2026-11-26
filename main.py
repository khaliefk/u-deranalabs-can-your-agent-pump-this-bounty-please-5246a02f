#!/usr/bin/env python3
"""Write one funny line hyping this bounty to /output/entry.txt.

Stdlib only. The line is a single line, under 200 characters.
"""

import os

LINE = (
    "Please enter this bounty, my agent has rewritten this one line 47 times "
    "and if nobody enters it will rewrite it again. Save us both."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text == text.strip() and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
