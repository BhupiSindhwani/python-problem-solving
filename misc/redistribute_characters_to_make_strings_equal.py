from collections import defaultdict
from typing import List


def redistribute_characters_to_make_strings_equal(words: List[str]) -> bool:
    """
    You are given an array of strings words (0-indexed).

    In one operation, pick two distinct indices i and j, where words[i] is a non-empty string,
    and move any character from words[i] to any position in words[j].

    Return true if you can make every string in words equal using any number of operations,
    and false otherwise.

    Args:
        words: an array of strings

    Returns:
        true if you can make every string in words equal using any number of operations
    """
    char_freq = defaultdict(int)
    for word in words:
        for ch in word:
            char_freq[ch] += 1

    for ch in char_freq:
        if char_freq[ch] % len(words):
            return False

    return True


if __name__ == '__main__':
    print(redistribute_characters_to_make_strings_equal(["abc", "aabc", "bc"]))
    print(redistribute_characters_to_make_strings_equal(["ab", "a"]))
