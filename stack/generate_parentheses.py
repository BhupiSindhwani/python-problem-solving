from typing import List


def generate_parentheses(n: int) -> List[str]:
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Args:
        n: input integer

    Returns:
        an array of strings with all combinations of well-formed parentheses based on input integer
    """
    # Backtracking solution
    stack = []
    result = []

    def backtrack(open_brackets, close_brackets):
        if open_brackets == close_brackets == n:
            result.append(''.join(stack))
            return

        if open_brackets < n:
            stack.append('(')
            backtrack(open_brackets + 1, close_brackets)
            stack.pop()

        if close_brackets < open_brackets:
            stack.append(')')
            backtrack(open_brackets, close_brackets + 1)
            stack.pop()

    backtrack(0, 0)
    return result

    # # Depth first search solution
    # output = []
    #
    # def dfs(left, right, stack, candidate):
    #
    #     # Base condition
    #     if left == right == 0:
    #         output.append(candidate)
    #         return
    #
    #     if left > 0:
    #         dfs(left - 1, right, stack + 1, candidate + '(')
    #
    #     if right > 0 and stack > 0:
    #         dfs(left, right - 1, stack - 1, candidate + ')')
    #
    # dfs(n, n, 0, '')
    #
    # return output


if __name__ == "__main__":
    print(generate_parentheses(3))
    print(generate_parentheses(1))
