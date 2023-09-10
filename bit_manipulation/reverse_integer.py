import math


def reverse_integer(x: int) -> int:
    """
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

    Args:
        x: a signed 32-bit integer

    Returns:
        x with its digits reversed
    """
    MIN = - (2 ** 31)
    MAX = (2 ** 31) - 1

    output = 0
    while x:
        digit = int(math.fmod(x, 10))  # using fmod to avoid python discrepancy with -ve numbers
        x = int(x / 10)  # using division with int to avoid python discrepancy with -ve numbers

        # Check to avoid running into situation of storing output beyond accepted MIN and MAX values
        if output > MAX // 10 or (output == MAX // 10 and digit > MAX % 10):
            return 0
        if output < MIN // 10 or (output == MIN // 10 and digit < MIN % 10):
            return 0

        output = (output * 10) + digit

    return output


if __name__ == "__main__":
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(1534236469))
