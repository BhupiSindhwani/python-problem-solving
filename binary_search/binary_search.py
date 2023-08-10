from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """
    Given an array of integers nums which is sorted in ascending order,
    and an integer target, write a function to search target in nums.

    If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.

    Args:
        nums: an array of integers sorted in ascending order
        target: integer target

    Returns:
        index if target exists, otherwise -1
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return mid

    return -1


if __name__ == "__main__":
    print(binary_search([-1, 0, 3, 5, 9, 12], 9))
    print(binary_search([-1, 0, 3, 5, 9, 12], 2))
    print(binary_search([5], 5))
    print(binary_search([], 5))
    print(binary_search([2, 5], 5))
