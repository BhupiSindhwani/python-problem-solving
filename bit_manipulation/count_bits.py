from typing import List


def count_bits(n: int) -> List[int]:
    """
    Given an integer n, return an 'ans' array of length n + 1 such that for each i (0 <= i <= n),
    ans[i] is the number of 1's in the binary representation of i.

    Args:
        n: an integer

    Returns:
        an array of length n + 1 such that each value represents the number of 1's in binary representation of index
    """
    ans = [0] * (n + 1)
    for idx in range(1, n + 1):
        ans[idx] = ans[idx // 2] + (idx % 2)

    return ans


if __name__ == "__main__":
    print(count_bits(2))
    print(count_bits(5))
