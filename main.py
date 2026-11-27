#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun one-liner entry.

Writes the printer's comeback line to entry.txt in the output directory.
Python 3.13 standard library only.
"""

import os

ENTRY = (
    "ERROR 0xE3, 214th occurrence. Cause: user. Action taken: none. "
    "I printed your resignation letter three times this year. "
    "You still work here."
)


def main() -> None:
    # Gate self-check: the competition requires 1 to 240 characters.
    if not 1 <= len(ENTRY) <= 240:
        raise SystemExit(
            f"ENTRY is {len(ENTRY)} characters; must be 1-240."
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
