def longest_palindromic_substring(s: str) -> str:
    """
    Given a string s, return the longest palindromic substring in s.

    Args:
        s: string

    Returns:
        the longest palindromic substring in input string
    """
    max_len, max_substring = 0, ''
    for idx, ch in enumerate(s):
        # odd length
        left, right = idx, idx
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                max_len = right - left + 1
                max_substring = s[left: right + 1]
            left -= 1
            right += 1

        # even length
        left, right = idx, idx + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                max_len = right - left + 1
                max_substring = s[left: right + 1]
            left -= 1
            right += 1

    return max_substring


if __name__ == '__main__':
    print(longest_palindromic_substring("babad"))
    print(longest_palindromic_substring("cbbd"))
    print(longest_palindromic_substring("cbbc"))
    print(longest_palindromic_substring("c"))
