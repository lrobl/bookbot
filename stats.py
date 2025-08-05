from typing import Dict, List


def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> Dict[str, int]:
    """Takes the text from the book as a string, and returns the number of times
    each character, (including symbols and spaces), appears in the string.
    Convert and character to lowercase.
    Use a dictionary of String -> Integer"""
    char_counts = {}
    for char in text:
        key = char.lower()
        # Add 1 to the current count, or 0 if the key is new
        char_counts[key] = char_counts.get(key, 0) + 1
    return char_counts


def format_chars_count(d: Dict[str, int]) -> List[Dict]:
    def _sort_on(item):
        return item["num"]

    chars = []
    for char, num in d.items():
        chars.append({"char": char, "num": num})

    chars.sort(reverse=True, key=_sort_on)
    return chars
