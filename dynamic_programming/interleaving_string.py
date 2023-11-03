def interleaving_string(s1: str, s2: str, s3: str) -> bool:
    """
    Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

    An interleaving of two strings s and t is a configuration where s and t are divided into n and m
    substrings respectively, such that:

    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
    Note: a + b is the concatenation of strings a and b.

    Args:
        s1: input string
        s2: input string
        s3: input string

    Returns:
        true if s3 is formed by an interleaving of s1 and s2; otherwise false
    """
    dp = {}

    def helper(ix1, ix2, ix3):
        # Base condition: accounting for all the strings
        if ix3 >= len(s3) and ix2 >= len(s2) and ix1 >= len(s1):
            return True

        # Check DP cache
        if (ix1, ix2) in dp:
            return dp[(ix1, ix2)]

        # Check s1
        s1_check = False
        if ix1 < len(s1) and ix3 < len(s3) and s1[ix1] == s3[ix3]:
            s1_check = helper(ix1 + 1, ix2, ix3 + 1)

        # Check s2
        s2_check = False
        if ix2 < len(s2) and ix3 < len(s3) and s2[ix2] == s3[ix3]:
            s2_check = helper(ix1, ix2 + 1, ix3 + 1)

        dp[(ix1, ix2)] = s1_check or s2_check
        return dp[(ix1, ix2)]

    return helper(0, 0, 0)


if __name__ == '__main__':
    print(interleaving_string("aabcc", "dbbca", "aadbbcbcac"))
    print(interleaving_string("aabcc", "dbbca", "aadbbbaccc"))
    print(interleaving_string("", "", ""))
    print(interleaving_string("a", "b", "a"))
    print(interleaving_string("aabcc", "dbbca", "aadbbcbacc"))
