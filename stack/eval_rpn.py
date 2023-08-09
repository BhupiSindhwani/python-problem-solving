from typing import List


def eval_rpn(tokens: List[str]) -> int:
    """
    You are given an array of strings tokens that represent an arithmetic expression in a Reverse Polish Notation.

    Evaluate the expression. Return an integer that represents the value of the expression.

    Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

    Args:
        tokens: an array of strings that represent an arithmetic expression

    Returns:
        an integer that represent the value of the expression
    """
    operators = '+-*/'
    stack = []

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            if token == '+':
                stack.append(operand_1 + operand_2)
            elif token == '-':
                stack.append(operand_1 - operand_2)
            elif token == '*':
                stack.append(operand_1 * operand_2)
            elif token == '/':
                stack.append(int(operand_1 / operand_2))

    return stack.pop()


if __name__ == "__main__":
    print(eval_rpn(["2", "1", "+", "3", "*"]))
    print(eval_rpn(["4", "13", "5", "/", "+"]))
    print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
    print(eval_rpn(["18"]))
