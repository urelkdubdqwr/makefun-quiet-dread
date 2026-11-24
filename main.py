"""Write the entry text to entry.txt in the output directory.

The output directory is $MAKEFUN_OUTPUT_DIR when set and non-empty,
otherwise /output. Standard library only; no network, randomness or clock.
"""

import os

ENTRY = (
    "LGTM. The linter is green, the CI is green, and I've begun to "
    "suspect green is a mood, not a state."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
