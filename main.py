"""Write the competition entry text to entry.txt in the output directory."""

import os

ENTRY_TEXT = (
    "The night the monsoon broke, we stood under a shop awning eating onion "
    "pakora from newspaper, and my father burned his fingers and said nothing, "
    "just handed me the biggest one."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
