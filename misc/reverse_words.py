def reverse_words(s: str) -> str:
    """
    Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace
    and initial word order.

    Args:
        s: input string

    Returns:
        string with each word reversed in the order
    """
    output = ' '.join(word[::-1] for word in s.split(" "))
    return output


if __name__ == "__main__":
    print(reverse_words("Let's take LeetCode contest"))
    print(reverse_words("God Ding"))
