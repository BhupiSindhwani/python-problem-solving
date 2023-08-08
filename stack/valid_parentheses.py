def valid_parentheses(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:

    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.

    Args:
        s: input string

    Returns:
        true if input string s consists of valid parentheses, otherwise false
    """
    open_braces = '([{'
    closed_braces = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []

    for ch in s:
        if ch in open_braces:
            stack.append(ch)
        else:
            if not stack or stack.pop() != closed_braces[ch]:
                return False

    return True if not stack else False


if __name__ == "__main__":
    print(valid_parentheses("()"))
    print(valid_parentheses("()[]{}"))
    print(valid_parentheses("()[{}]"))
    print(valid_parentheses("()[{]}"))
    print(valid_parentheses("()[}{]"))
    print(valid_parentheses("(]"))
