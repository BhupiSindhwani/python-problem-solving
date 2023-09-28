import math


def decoded_string_at_index(s: str, k: int) -> str:
    """
    You are given an encoded string s. To decode the string to a tape, the encoded string is read one character
    at a time and the following steps are taken:

    If the character read is a letter, that letter is written onto the tape.
    If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
    Given an integer k, return the kth letter (1-indexed) in the decoded string.

    Args:
        s: input string
        k: an integer

    Returns:
        kth letter (1-indexed) in the decoded string
    """
    count = 0

    for ch in s:
        if ch.isdigit():
            count *= int(ch)
        else:
            count += 1

    for ch in s[::-1]:
        k %= count
        if ch.isdigit():
            count //= int(ch)
        else:
            if k == 0:
                return ch
            else:
                count -= 1


if __name__ == "__main__":
    print(decoded_string_at_index("leet2code3", 10))
    print(decoded_string_at_index("leet2code3", 15))
    print(decoded_string_at_index("ha22", 5))
    print(decoded_string_at_index("a2345678999999999999999", 1))
    print(decoded_string_at_index("y959q969u3hb22odq595", 222280369))
