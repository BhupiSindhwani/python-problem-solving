from typing import List


def missing_number(nums: List[int]) -> int:
    """
    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.

    Args:
        nums: an array containing n distinct numbers in the range [0, n]

    Returns:
        only number in the range that is missing from the input array
    """
    n = len(nums)
    output = int((n * (n+1)) / 2)
    for num in nums:
        output -= num
    return output

    # # Solution using XOR
    # n = len(nums)
    # output = 0
    # for idx in range(n):
    #     output ^= idx + 1 ^ nums[idx]
    #
    # return output


if __name__ == "__main__":
    print(missing_number([3, 0, 1]))
    print(missing_number([0, 1]))
    print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
