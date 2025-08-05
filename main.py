import sys
from stats import count_chars, count_words, format_chars_count


def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as f:
        file_contents = f.read()
    return file_contents


def main(book_file_path: str):

    # Read the book
    book_contents = get_book_text(book_file_path)

    # Count the words
    word_count = count_words(book_contents)

    # Count the characters
    char_count = count_chars(book_contents)

    # Format and sort the character report
    chars = format_chars_count(char_count)

    # Create and print the report
    report = f"""
============ BOOKBOT ============
Analyzing book found at {book_file_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------"""
    for d in chars:
        if d["char"].isalpha():
            report += f"""\n{d["char"]}: {d["num"]}"""
    report += """
============= END ==============="""
    print(report)


if __name__ == "__main__":
    args = sys.argv

    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(book_file_path=args[1])
