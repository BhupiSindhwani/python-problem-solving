def multiply_strings(num1: str, num2: str) -> str:
    """
    Given two non-negative integers num1 and num2 represented as strings,
    return the product of num1 and num2, also represented as a string.

    Note: You must not use any built-in library or convert the inputs to integer directly.

    Args:
        num1: a non-negative integer, represented as a sting
        num2: a non-negative integer, represented as a sting

    Returns:
        the product of num1 and num2, represented as a string
    """
    if "0" in [num1, num2]:
        return "0"

    result = [0] * (len(num1) + len(num2))
    num1, num2 = num1[::-1], num2[::-1]
    for idx1 in range(len(num1)):
        for idx2 in range(len(num2)):
            digit = int(num1[idx1]) * int(num2[idx2])
            result[idx1 + idx2] += digit
            result[idx1 + idx2 + 1] += (result[idx1 + idx2] // 10)
            result[idx1 + idx2] %= 10

    result, beg = result[::-1], 0
    while beg < len(result) and result[beg] == 0:
        beg += 1

    result = map(str, result[beg:])
    return ''.join(result)


if __name__ == "__main__":
    print(multiply_strings("2", "3"))
    print(multiply_strings("123", "456"))
