#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes the entry's single one-line office joke to /output/entry.txt,
where the house judge reads it.
"""

import os

JOKE = "Management replaced the dead office plants with a poster of a forest and called it our wellness program."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
