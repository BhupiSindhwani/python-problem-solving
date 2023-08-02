def valid_anagram(s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    Args:
        s: input string
        t: input string

    Returns:
       return true if t is an anagram of s, otherwise false
    """
    char_count = {}
    for s_ch in s:
        char_count[s_ch] = char_count.get(s_ch, 0) + 1

    for t_ch in t:
        if t_ch in char_count:
            char_count[t_ch] -= 1
            if char_count[t_ch] <= 0:
                del char_count[t_ch]
        else:
            return False

    return True if not char_count else False


if __name__ == "__main__":
    print(valid_anagram("anagram", "nagaram"))
    print(valid_anagram("rat", "car"))
    print(valid_anagram("ab", "a"))
    print(valid_anagram("a", "ab"))
