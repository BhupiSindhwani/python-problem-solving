import string


def valid_palindrome(s: str) -> bool:
    """
    Given a string s, return true if it is a palindrome, or false otherwise.

    Args:
        s: input string

    Returns:
        true if s is a palindrome, otherwise false
    """
    start = 0
    end = len(s) - 1

    while start < end:
        if not s[start].isalnum():
            start += 1
            continue
        if not s[end].isalnum():
            end -= 1
            continue
        if s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1

    return True


if __name__ == "__main__":
    print(valid_palindrome("A man, a plan, a canal: Panama"))
    print(valid_palindrome("race a car"))
    print(valid_palindrome(" "))
    print(valid_palindrome("0P"))
