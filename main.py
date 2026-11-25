"""Write the competition entry text to entry.txt in the output directory.

The output directory is MAKEFUN_OUTPUT_DIR when set and non-empty, otherwise
the literal path /output. The directory is created if it does not exist.
"""

import os
import sys

ENTRY_TEXT = (
    "The night the monsoon broke, we stood under a shop awning eating onion "
    "pakora from newspaper, and my father burned his fingers and said nothing, "
    "just handed me the biggest one."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as error:
        print(f"error: cannot create output directory {output_dir!r}: {error}", file=sys.stderr)
        return 1
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
