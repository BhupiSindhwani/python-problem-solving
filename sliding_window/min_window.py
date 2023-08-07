def min_window(s: str, t: str) -> str:
    """
    Given two strings s and t of lengths m and n respectively, return the minimum window substring
    of s such that every character in t (including duplicates) is included in the window. If there is no such substring,
    return the empty string "".

    Args:
        s: string
        t: string

    Returns:
        minimum window substring of s such that every character in t (includes duplicates) is included, otherwise
        return empty string
    """
    if not t or len(s) < len(t):
        return ""

    t_freq = {}
    for ch in t:
        t_freq[ch] = t_freq.get(ch, 0) + 1

    win_freq = {}
    start = 0
    matches = 0
    result = ""
    min_len = float("infinity")

    for end in range(len(s)):

        if s[end] in t_freq:
            win_freq[s[end]] = win_freq.get(s[end], 0) + 1
            if win_freq[s[end]] == t_freq[s[end]]:
                matches += 1

        while matches == len(t_freq):
            if end - start + 1 < min_len:
                result = s[start: end + 1]
                min_len = end - start + 1

            if s[start] in win_freq:
                win_freq[s[start]] -= 1
                if win_freq[s[start]] < t_freq[s[start]]:
                    matches -= 1
            start += 1

            while start < end and s[start] not in t_freq:
                start += 1

    return result if min_len != float("infinity") else ""


if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))
    print(min_window("a", "a"))
    print(min_window("a", "aa"))
    print(min_window("ab", "a"))
    print(min_window("ab", "b"))
    print(min_window("aa", "aa"))
