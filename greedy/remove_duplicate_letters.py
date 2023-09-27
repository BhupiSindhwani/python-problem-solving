def remove_duplicate_letters(s: str) -> str:
    """
    Given a string s, remove duplicate letters so that every letter appears once and only once.
    You must make sure your result is the smallest in lexicographical order among all possible results.

    Args:
        s: input string

    Returns:
        string (smallest in lexicographical order among all possible results) by removing duplicate letters
    """
    output_stack = []
    output_set = set()
    char_freq = {}

    for ch in s:
        char_freq[ch] = char_freq.get(ch, 0) + 1

    for ch in s:
        char_freq[ch] -= 1

        if ch in output_set:
            continue

        while output_stack and ch < output_stack[-1] and char_freq[output_stack[-1]] > 0:
            output_set.remove(output_stack[-1])
            output_stack.pop()

        output_stack.append(ch)
        output_set.add(ch)

    return ''.join(output_stack)


if __name__ == "__main__":
    print(remove_duplicate_letters("bcabc"))
    print(remove_duplicate_letters("bcdbca"))
    print(remove_duplicate_letters("cbacdcbc"))
    print(remove_duplicate_letters("bbcaac"))
    print(remove_duplicate_letters("abacb"))
