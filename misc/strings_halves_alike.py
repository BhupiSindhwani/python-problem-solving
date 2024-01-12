def strings_halves_alike(s: str) -> bool:
    """
    You are given a string s of even length. Split this string into two halves of equal
    lengths, and let a be the first half and b be the second half.

    Two strings are alike if they have the same number of vowels
    ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
    Notice that s contains uppercase and lowercase letters.

    Return true if a and b are alike. Otherwise, return false.

    Args:
        s: input string of even length

    Returns:
        True if input string can be split into two equal halves with same number of vowels
    """
    vowels = set(list('aeiouAEIOU'))
    # print(vowels)
    vowels_count = 0
    vowels_left_count = 0
    for idx, ch in enumerate(s):
        if idx == len(s) // 2:
            vowels_left_count = vowels_count
        if ch in vowels:
            vowels_count += 1

    return True if vowels_count == 2 * vowels_left_count else False


if __name__ == '__main__':
    print(strings_halves_alike("tkPAdxpMfJiltOerItiv"))
    print(strings_halves_alike("book"))
    print(strings_halves_alike("textbook"))
