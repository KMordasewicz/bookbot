"""Module for text analysis."""

def word_count(text: str) -> int:
    """Function to count words in a given text."""

    return len(text.split())


def char_count(text: str) -> dict[str, int]:
    """Function to count apperance of each character in a given text."""
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict


def sort_dict(d: dict[str, int|float]) -> list[dict[str, int|float]]:
    def sort_on(d: dict):
        return list(d.values())[0]

    dict_list = [{k: v} for k, v in d.items()]
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list
