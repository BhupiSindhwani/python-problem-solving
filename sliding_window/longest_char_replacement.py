def longest_char_replacement(s: str, k: int) -> int:
    """
    You are given a string s and an integer k. You can choose any character of the string and change
    it to any other uppercase English character. You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter
    you can get after performing the above operations.

    Args:
        s: input string consisting of only uppercase English letters.
        k: integer

    Returns:
        length of the longest substring containing the same letter after performing k operations
    """
    start, end = 0, 0

    max_len = 0
    char_freq = {}

    while end < len(s):
        char_freq[s[end]] = char_freq.get(s[end], 0) + 1
        if (end - start + 1) - max(char_freq.values()) > k:
            char_freq[s[start]] -= 1
            if char_freq[s[start]] == 0:
                del char_freq[s[start]]
            start += 1
        end += 1

    return max(max_len, end - start)


if __name__ == "__main__":
    print(longest_char_replacement("ABAB", 2))
    print(longest_char_replacement("AABABBA", 1))
    print(longest_char_replacement("AABAABBA", 1))
