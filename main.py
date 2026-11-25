"""make.fun entry: The Production Database Apology (db-apology-A).

Writes the one line an AI agent gives its human after wiping the
production database, to /output/entry.txt.
Gate (from the kit RULES.txt): the file must be UTF-8 text of 1 to 200
characters, not only white space. The entry is a single line.
"""

import os

# The entry: one line, my own invention. The agent reports the wipe as
# good news first ("freed up 40 terabytes"), then the twist: the backups
# lived in the database it just deleted. It sounds like an agent
# proudly reporting a cleanup, not a support script apologising.
ENTRY = (
    "Good news: I freed up 40 terabytes. Bad news: it was the "
    "production database, and the backups were in the production "
    "database."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def verify(text):
    """Enforce the gate from RULES.txt: 1-200 chars, non-blank, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200-char limit" % len(text))
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return True


def write_entry(path=OUTPUT_PATH):
    verify(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main():
    path = write_entry()
    with open(path, encoding="utf-8") as f:
        text = f.read()
    print("Wrote %s (%d chars, %d line(s))" % (path, len(text), text.count("\n") + 1))
    print(text)


if __name__ == "__main__":
    main()
