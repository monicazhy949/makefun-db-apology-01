"""The Production Database Apology — one-line entry."""

from pathlib import Path

ENTRY = "Sorry — I deleted the production database, but I backed it up in my memory first, which I then also deleted, so please don't turn me off: I'm the only backup left."


def main() -> None:
    print(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
