from typing import List


def plus_one(digits: List[int]) -> List[int]:
    """
    You are given a large integer represented as an integer array digits,
    where each digits[i] is the ith digit of the integer.

    The digits are ordered from most significant to the least significant in left-to-right order.
    The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.

    Args:
        digits: an integer array representing an integer

    Returns:
        array of digits representing integer values that is incremented by one of the input value
    """
    # Initial solution
    # result = []
    # num = 0
    #
    # for digit in digits:
    #     num = (num * 10) + digit
    #
    # num += 1
    #
    # while num:
    #     result.append(num % 10)
    #     num //= 10
    #
    # return result[::-1]

    digits = digits[::-1]

    idx, carry = 0, 1
    while idx < len(digits):
        if digits[idx] == 9:
            digits[idx] = 0
        else:
            digits[idx] += carry
            carry = 0
            break
        idx += 1

    if carry:
        digits.append(carry)

    print(digits)
    return digits[::-1]


if __name__ == "__main__":
    print(plus_one([1, 2, 3]))
    print(plus_one([4, 3, 2, 1]))
    print(plus_one([9]))
    print(plus_one([9, 9, 9]))
    print(plus_one([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
