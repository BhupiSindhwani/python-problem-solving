from typing import List


def min_size_subarray_sum(target: int, nums: List[int]) -> int:
    """
    Given an array of positive integers nums and a positive integer target, return the minimal length of a
    subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

    Args:
        target: a positive integer target
        nums: an array of positive integers

    Returns:
        the minimal length of a subarray whose sum >= target; otherwise return 0
    """
    min_count = float('inf')
    left, right, curr_sum = 0, 0, 0

    while right < len(nums):
        curr_sum += nums[right]
        while curr_sum >= target:
            min_count = min(min_count, right - left + 1)
            curr_sum -= nums[left]
            left += 1
        right += 1

    return 0 if min_count == float('inf') else min_count


if __name__ == '__main__':
    print(min_size_subarray_sum(7, [2, 3, 1, 2, 4, 3]))
    print(min_size_subarray_sum(4, [1, 4, 4]))
    print(min_size_subarray_sum(11, [1, 1, 1, 1, 1, 1, 1, 1]))
    print(min_size_subarray_sum(11, [1, 2, 3, 4, 5]))
