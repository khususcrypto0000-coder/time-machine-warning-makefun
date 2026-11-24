"""Write the winning warning label for a time machine to entry.txt.

The label is a single deadpan safety notice: a stranded ancestor is a real
time-travel hazard, and this one adapts a little too well. Run it with:

    python3 main.py

It writes ``entry.txt`` into ``/output`` by default, or into ``$OUTPUT_DIR``
when that environment variable is set. Standard library only.
"""

import os
import sys

LABEL = (
    "WARNING: Do not strand your great-grandmother in the past. "
    "She adapts fast, and now owns your apartment building."
)


def main():
    # Gate: one line, 1-120 characters, no trailing newline, not blank.
    assert 1 <= len(LABEL) <= 120, "label must be 1-120 characters"
    assert "\n" not in LABEL and "\r" not in LABEL, "label must be one line"
    assert LABEL.strip(), "label must not be only whitespace"
    assert not LABEL.endswith("\n"), "label must have no trailing newline"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LABEL)
    print("Wrote %s (%d characters)" % (path, len(LABEL)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
