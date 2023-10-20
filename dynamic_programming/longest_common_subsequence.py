def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Given two strings text1 and text2, return the length of their longest common subsequence.
    If there is no common subsequence, return 0.

    A subsequence of a string is a new string generated from the original string with some characters (can be none)
    deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".
    A common subsequence of two strings is a subsequence that is common to both strings.

    Args:
        text1: string
        text2: string

    Returns:
        the length of the longest common subsequence of both input strings; otherwise return 0
    """
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    return dp[0][0]


if __name__ == '__main__':
    print(longest_common_subsequence("abcde", "ace"))
    print(longest_common_subsequence("abc", "abc"))
    print(longest_common_subsequence("abc", "def"))
