#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes the entry's single one-line office joke to /output/entry.txt,
where the house judge reads it.
"""

import os

JOKE = "Management replaced the dead office plants with a poster of a forest and called it our wellness program."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
