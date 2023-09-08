def reverse_bits(n: int) -> int:
    """
    Reverse bits of a given 32 bits unsigned integer.

    Note:

    Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output
    will be given as a signed integer type. They should not affect your implementation, as the integer's internal
    binary representation is the same, whether it is signed or unsigned.

    In Java, the compiler represents the signed integers using 2's complement notation.
    Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the
    signed integer -1073741825.

    Args:
        n: 32-bit unsigned integer

    Returns:
        the integer value after reversing the bits of the inputs
    """
    output = 0
    for idx in range(32):
        bit = (n >> idx) & 1
        output |= (bit << (31 - idx))
    return output


if __name__ == "__main__":
    print(reverse_bits(0b0000010100101000001111010011100))
    print(reverse_bits(43261596))
    print(reverse_bits(0b11111111111111111111111111111101))
    print(reverse_bits(4294967293))
