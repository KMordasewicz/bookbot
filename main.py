"""Main fucntion of BookBot package."""



def get_book_text(path: str) -> str:
    """Function to read file context from given path."""
    with open(path) as f:
        f_content = f.read()

    return f_content


def word_count(text: str) -> int:
    """Function to count words in a given text."""

    return len(text.split())


def main():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_content = get_book_text(frankenstein_path)
    wc = word_count(frankenstein_content)

    print(f"{wc} words found in the document")


if __name__ == "__main__":
    main()
