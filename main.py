def main():
    book_path = "books/frankenstein.txt"
    book = read_book(book_path)

    # Print out Report
    print(f"""--- Begin report of {book_path} ---""")
    print(f"""{count_words(book)} words found in the document\n""")

    letter_count = count_letters(book)
    for letter in letter_count:
        print(f"The '{letter}' character was found {letter_count[letter]} times")
    print("--- End report---")


def read_book(path):
    with open(path) as file:
        file_contents = file.read()
    return file_contents


def count_words(book):
    words = book.split()
    return len(words)


def count_letters(book):
    letters = {chr(ord("a") + i): 0 for i in range(0, 26)}

    for character in book:
        character = character.lower()
        if character in letters:
            letters[character] += 1
    return letters


main()
