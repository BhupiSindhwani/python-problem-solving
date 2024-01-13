from collections import defaultdict


def min_steps_to_make_two_strings_anagram(s: str, t: str) -> int:
    """
    You are given two strings of the same length s and t. In one step you can choose
    any character of t and replace it with another character.

    Return the minimum number of steps to make t an anagram of s.

    An Anagram of a string is a string that contains the same characters with a
    different (or the same) ordering.

    Args:
        s: input string
        t: input string

    Returns:
        the minimum number of steps to make t an anagram of s
    """
    # Initial Solution
    # num_steps = 0
    # s_char_freq = defaultdict(int)
    # for ch in s:
    #     s_char_freq[ch] += 1

    # for ch in t:
    #     if ch in s_char_freq:
    #         s_char_freq[ch] -= 1
    #         if s_char_freq[ch] == 0:
    #             del s_char_freq[ch]
    #     else:
    #         num_steps += 1

    # return num_steps

    num_steps = 0

    char_freq = defaultdict(int)

    for idx in range(len(s)):
        char_freq[s[idx]] += 1
        char_freq[t[idx]] -= 1

    # print(char_freq)
    for char in char_freq:
        if char_freq[char] > 0:
            num_steps += char_freq[char]

    return num_steps


if __name__ == '__main__':
    print(min_steps_to_make_two_strings_anagram("leetcode", "practice"))
    print(min_steps_to_make_two_strings_anagram("gctcxyuluxjuxnsvmomavutrrfb", "qijrjrhqqjxjtprybrzpyfyqtzf"))
