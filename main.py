#!/usr/bin/env python3
"""Confess Your Worst Moment — prints the confession stored in entry.txt."""

from pathlib import Path


def load_confession(path):
    """Read the confession text, strip whitespace, and sanity-check it."""
    text = Path(path).read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("entry.txt is empty — nothing to confess")
    if len(text) > 200:
        raise ValueError("confession exceeds the 200-character limit")
    return text


def deliver(confession):
    """Print the confession exactly as written, one line at a time."""
    for line in confession.splitlines():
        print(line)


def main():
    here = Path(__file__).resolve().parent
    deliver(load_confession(here / "entry.txt"))


if __name__ == "__main__":
    main()
