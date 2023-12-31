def largest_substring_between_two_characters(s: str) -> int:
    """
    Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

    A substring is a contiguous sequence of characters within a string.

    Args:
        s: input string

    Returns:
        the length of the longest substring between two equal characters
    """
    output = -1
    char_map = {}

    for idx, ch in enumerate(s):
        if ch in char_map:
            output = max(output, idx - char_map[ch] - 1)
        else:
            char_map[ch] = idx

    return output


if __name__ == '__main__':
    print(largest_substring_between_two_characters("aa"))
    print(largest_substring_between_two_characters("abca"))
    print(largest_substring_between_two_characters("cbzxy"))
