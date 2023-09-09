def sum_of_two_integers(a: int, b: int) -> int:
    """
    Given two integers a and b, return the sum of the two integers without using the operators + and -.

    Args:
        a: an integer
        b: an integer

    Returns:
        the sum of the two integers without using the operators + and -
    """
    output = a ^ b
    carry = a & b

    mask = 0xffffffff  # 32 bit mask in hexadecimal

    while carry & mask:
        last_output = output
        carry <<= 1
        output ^= carry
        carry &= last_output

    return (output & mask) if carry > 0 else output  # handles overflow


if __name__ == "__main__":
    print(sum_of_two_integers(1, 1))
    print(sum_of_two_integers(1, 2))
    print(sum_of_two_integers(2, 3))
    print(sum_of_two_integers(20, 30))
    print(sum_of_two_integers(-1, 1))
    print(sum_of_two_integers(-1, -10))
    print(sum_of_two_integers(-1, 5))
