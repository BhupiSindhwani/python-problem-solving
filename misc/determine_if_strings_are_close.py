from collections import defaultdict, Counter


def determine_if_strings_are_close(word1: str, word2: str) -> bool:
    """
    Two strings are considered close if you can attain one from the other using the following operations:

    Operation 1: Swap any two existing characters.
    For example, abcde -> aecdb
    Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
    For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
    You can use the operations on either string as many times as necessary.

    Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

    Args:
        word1: input word1
        word2: input word2

    Returns:
        ture if word1 and word2 are close based on the above rules
    """
    # Initial Solution
    # if len(word1) != len(word2):
    #     return False

    # word1_char_freq = [0] * 26
    # word2_char_freq = [0] * 26

    # word1_char_set = set()
    # word2_char_set = set()

    # for idx in range(len(word1)):
    #     word1_char_freq[ord(word1[idx]) - ord('a')] += 1
    #     word1_char_set.add(word1[idx])
    #     word2_char_freq[ord(word2[idx]) - ord('a')] += 1
    #     word2_char_set.add(word2[idx])

    # word1_char_freq.sort()
    # word2_char_freq.sort()

    # return word1_char_freq == word2_char_freq and word1_char_set == word2_char_set

    if len(word1) != len(word2):
        return False

    word1_char_freq = defaultdict(int)
    word2_char_freq = defaultdict(int)

    for idx in range(len(word1)):
        word1_char_freq[word1[idx]] += 1
        word2_char_freq[word2[idx]] += 1

    word1_count_freq = Counter(word1_char_freq.values())
    word2_count_freq = Counter(word2_char_freq.values())

    return word1_char_freq.keys() == word2_char_freq.keys() and word1_count_freq == word2_count_freq


if __name__ == '__main__':
    print(determine_if_strings_are_close("cabbba", "abbccc"))
    print(determine_if_strings_are_close("cabbba", "aabbss"))
