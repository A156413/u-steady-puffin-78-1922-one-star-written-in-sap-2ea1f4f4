"""One Star, Written in Sap — a houseplant's 1-star review of its human owner."""

import os

ENTRY = "One star. He waters me once a month with a coffee mug, then brags to guests that I'm 'low maintenance.' I'm not low maintenance — I'm dehydrated, sunburned, and named after his ex. Would not photosynthesize here again."

assert len(ENTRY) < 280, f"entry is {len(ENTRY)} chars, must be under 280"


def main():
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
