from typing import List


def backspace_string_compare(s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if they are equal when both are typed into empty text editors.
    '#' means a backspace character.

    Note that after backspacing an empty text, the text will continue empty.

    Args:
        s: string
        t: string

    Returns:
        true if both input string are equal when typed into empty text editors
    """
    # # Solution using stacks
    # def process_string(input_string: str) -> List[str]:
    #     stack = []
    #     for ch in input_string:
    #         if ch == '#':
    #             if len(stack) > 0:
    #                 stack.pop()
    #         else:
    #             stack.append(ch)
    #     return stack
    #
    # return process_string(s) == process_string(t)

    # Improved Solution with O(1) space complexity
    def next_char(input_string: str, idx_ptr: int) -> int:
        backspace_count = 0
        while idx_ptr >= 0:
            if input_string[idx_ptr] == '#':
                backspace_count += 1
            elif backspace_count > 0:
                backspace_count -= 1
            else:
                break
            idx_ptr -= 1
        return idx_ptr

    ps, pt = len(s) - 1, len(t) - 1
    while ps >= 0 or pt >= 0:
        ps = next_char(s, ps)
        pt = next_char(t, pt)

        if ps < 0 and pt < 0:
            return True
        if ps < 0 or pt < 0:
            return False
        elif s[ps] != t[pt]:
            return False

        ps -= 1
        pt -= 1

    return True


if __name__ == '__main__':
    print(backspace_string_compare("ab#c", "ad#c"))
    print(backspace_string_compare("ab##", "c#d#"))
    print(backspace_string_compare("a#c", "b"))
    print(backspace_string_compare("xywrrmp", "xywrrmu#p"))
