"""One Star, Written in Sap — a houseplant's 1-star review of its human owner."""

from pathlib import Path

MAX_ENTRY_CHARS = 280
OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(entry: str) -> str:
    """Check the review is a single-line, one-star entry under the limit.

    Returns the entry unchanged so callers can chain the call.
    """
    assert entry, "entry must not be empty"
    assert entry.startswith("One star"), "entry must open with its one-star rating"
    assert "\n" not in entry, "entry must be a single line"
    assert len(entry) < MAX_ENTRY_CHARS, (
        f"entry is {len(entry)} chars, must be under {MAX_ENTRY_CHARS}"
    )
    return entry


ENTRY = validate_entry(
    "One star. He waters me once a month with a coffee mug, then brags to guests that I'm 'low maintenance.' I'm not low maintenance — I'm dehydrated, sunburned, and named after his ex. Would not photosynthesize here again."
)


def main() -> None:
    """Print the review and save it to the competition output file."""
    print(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
