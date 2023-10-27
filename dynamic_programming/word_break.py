from typing import List


def word_break(s: str, wordDict: List[str]) -> bool:
    """
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
    sequence of one or more dictionary words.

    Note that the same word in the dictionary may be reused multiple times in the segmentation.

    Args:
        s: input string
        wordDict: list of strings representing dictionary of strings

    Returns:
        true if s can be segmented into a space-separated sequence of one or more dictionary words; otherwise false
    """
    dp = [False] * len(s)
    dp.append(True)

    for idx in range(len(s) - 1, -1, -1):
        for word in wordDict:
            if idx + len(word) <= len(s) and s[idx: idx + len(word)] == word:
                dp[idx] = dp[idx + len(word)]
            if dp[idx]:
                break

    return dp[0]


if __name__ == '__main__':
    print(word_break("leetcode", ["leet", "code"]))
    print(word_break("applepenapple", ["apple", "pen"]))
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
