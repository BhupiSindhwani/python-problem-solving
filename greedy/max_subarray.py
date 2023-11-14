from typing import List


def max_subarray(nums: List[int]) -> int:
    """
    Given an integer array nums, find the subarray with the largest sum, and return its sum.

    Args:
        nums: an integer array

    Returns:
        sum of the subarray with the largest sum
    """
    # # Initial Solution
    # max_sum = nums[0]
    #
    # curr_sum = 0
    # for num in nums:
    #     curr_sum += num
    #     max_sum = max(max_sum, curr_sum)
    #     if curr_sum < 0:
    #         curr_sum = 0
    #
    # return max_sum

    # Refactored Solution
    max_sum = float('-inf')
    curr_sum = 0

    for num in nums:
        curr_sum += num
        if curr_sum <= num:
            curr_sum = num
        max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_subarray([1]))
    print(max_subarray([5, 4, -1, 7, 8]))
    print(max_subarray([-2, 1]))
    print(max_subarray([-2, -1]))
    print(max_subarray([-2, -3, -1]))
    print(max_subarray([-2, 3, 1, 3]))
