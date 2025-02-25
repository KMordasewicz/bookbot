"""Main fucntion of BookBot package."""
import sys
from stats import word_count, char_count, sort_dict



def get_book_text(path: str) -> str:
    """Function to read file context from given path."""
    with open(path) as f:
        f_content = f.read()

    return f_content


def main(path: str) -> None:
    book_path = path
    book_content = get_book_text(book_path)
    wc = word_count(book_content)
    cc = char_count(book_content)
    ccl = sort_dict(cc)
    ccl = sort_dict(cc)

    # Report:
    print(12*"=", " BOOKBOT ", 12*"=")
    print(f"Analyzing book found at {book_path}...")
    print(11*"-", " Word Count ", 11*"-")
    print(f"Found {wc} total words")
    print(10*"-", " Character Count ", 10*"-")
    for counter_characters in ccl:
        key, value = counter_characters.popitem()
        if key.isalpha():
            print(f"{key}: {value}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(sys.argv[1])


