def palindromic_substrings(s: str) -> int:
    """
    Given a string s, return the number of palindromic substrings in it.

    A string is a palindrome when it reads the same backward as forward.
    A substring is a contiguous sequence of characters within the string.

    Args:
        s: string

    Returns:
        the number of palindromic substrings in input string
    """
    count = 0

    for idx in range(len(s)):
        for left, right in ((idx, idx), (idx, idx + 1)):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

    return count


if __name__ == '__main__':
    print(palindromic_substrings("abc"))
    print(palindromic_substrings("aaa"))
