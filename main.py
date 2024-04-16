def main():
    book = read_book("books/frankenstein.txt")
    print(count_words(book))


def read_book(path):
    with open(path) as file:
        file_contents = file.read()
    return file_contents


def count_words(book):
    words = book.split()
    return len(words)


main()
