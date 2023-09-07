def hamming_weight(n: int) -> int:
    """
    Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits
    it has (also known as the Hamming weight).

    Note:

    Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be
    given as a signed integer type. It should not affect your implementation, as the integer's internal binary
    representation is the same, whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation.
    Therefore, in Example 3, the input represents the signed integer. -3.

    Args:
        n: binary representation of an unsigned integer

    Returns:
        the number of '1' bits in the input
    """
    # # Initial Solution
    # count = 0
    # for ch in bin(n):
    #     count += 1 if ch == '1' else 0
    #
    # return count

    count = 0
    while n:
        count += n % 2
        n >>= 1   # bitwise right shift
    return count

    # # Non-intuitive solution
    # count = 0
    # while n:
    #     n &= n - 1
    #     count += 1
    # return count


if __name__ == "__main__":
    print(hamming_weight(0o0000000000000000000000000001011))
    print(hamming_weight(0o0000000000000000000000010000000))
    print(hamming_weight(0o11111111111111111111111111111101))
