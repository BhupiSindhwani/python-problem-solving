def permutation_in_string(s1: str, s2: str) -> bool:
    """
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of s2.

    Args:
        s1: string
        s2: string

    Returns:
        true if one of s1's permutations is the substring of s2
    """
    if len(s1) > len(s2):
        return False

    s1_freq, s2_freq = {}, {}
    matches = 0

    for idx in range(len(s1)):
        s1_freq[s1[idx]] = s1_freq.get(s1[idx], 0) + 1
        s2_freq[s2[idx]] = s2_freq.get(s2[idx], 0) + 1

    for _ in s1_freq:
        if _ in s2_freq and s2_freq[_] == s1_freq[_]:
            matches += 1

    start = 0

    for end in range(len(s1), len(s2)):
        if matches == len(s1_freq):
            return True

        s2_freq[s2[end]] = s2_freq.get(s2[end], 0) + 1
        if s2[end] in s1_freq and s1_freq[s2[end]] == s2_freq[s2[end]]:
            matches += 1
        elif s2[end] in s1_freq and s1_freq[s2[end]] + 1 == s2_freq[s2[end]]:
            matches -= 1

        s2_freq[s2[start]] = s2_freq.get(s2[start], 0) - 1
        if s2[start] in s1_freq and s1_freq[s2[start]] == s2_freq[s2[start]]:
            matches += 1
        elif s2[start] in s1_freq and s1_freq[s2[start]] - 1 == s2_freq[s2[start]]:
            matches -= 1

        start += 1

    return matches == len(s1_freq)


if __name__ == "__main__":
    print(permutation_in_string("ab", "eidbaooo"))
    print(permutation_in_string("ab", "eidboaoo"))
    print(permutation_in_string("abcdxabcde", "abcdeabcdx"))
