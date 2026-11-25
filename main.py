"""Unsent: The Micro-Confession Sprint — entry program.

Writes one original two-part micro-confession to the output file:
a To: line naming who it was meant for, and the unsent message itself,
one line written exactly as it was typed, with no explanation after it.

Pure Python standard library. No network, no input, no environment
reads. The text is a constant, so every run writes identical bytes.
"""

from pathlib import Path

CONFESSION = (
    "To: my older brother, who still thinks I left home for the money\n"
    "come home for Eid, I'll cook. i miss you more than i miss being right"
)

def pick_output_path() -> Path:
    """Prefer the sandbox output directory when it already exists.

    Creating a top-level directory is never attempted: on a machine
    without the sandbox mount, the entry lands beside the program.
    """
    sandbox = Path("/output")
    if sandbox.is_dir():
        return sandbox / "entry.txt"
    return Path(__file__).resolve().parent / "output" / "entry.txt"


def main() -> int:
    text = CONFESSION
    lines = text.split("\n")
    assert len(lines) == 2, "entry must be exactly two parts"
    assert 1 <= len(text) <= 260, "gate: 1 to 260 characters"
    assert len(lines[1]) <= 200, "message line at most 200 characters"
    assert text.strip(), "entry must not be only white space"
    path = pick_output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"wrote {path}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
