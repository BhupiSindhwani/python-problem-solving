def longest_substring(s: str) -> int:
    """
    Given a string s, find the length of the longest substring
    without repeating characters.

    Args:
        s: input string

    Returns:
        length of the longest substring without repeating characters
    """
    if not s:
        return 0

    left, right = 0, 0
    char_set = set()

    max_len_substring = 0

    while right < len(s):
        if s[right] not in char_set:
            char_set.add(s[right])
        else:
            max_len_substring = max(max_len_substring, right - left)
            while s[left] != s[right]:
                char_set.remove(s[left])
                left += 1
            left += 1
        right += 1

    return max(max_len_substring, right - left)


if __name__ == "__main__":
    print(longest_substring("abcabcbb"))
    print(longest_substring("bbbbb"))
    print(longest_substring("pwwkew"))
    print(longest_substring(""))
    print(longest_substring("au"))
    print(longest_substring("ggububgvfk"))
