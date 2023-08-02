import collections
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Given an array of strings strs, group the anagrams together.

    Args:
        strs: an array of strings

    Returns:
        group of anagrams from input array of strings
    """
    anagram_dict = collections.defaultdict(list)

    for st in strs:
        sorted_str = ''.join(sorted(st))
        anagram_dict[sorted_str].append(st)

    anagrams_groups = []
    for anagram in anagram_dict:
        anagrams_groups.append(anagram_dict[anagram])

    return anagrams_groups


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(group_anagrams([""]))
    print(group_anagrams(["a"]))
