def main():
    book = read_book("books/frankenstein.txt")
    print(count_letters(book))


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
