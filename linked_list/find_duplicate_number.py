from typing import List


def find_duplicate_number(nums: List[int]) -> int:
    """
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.

    Args:
        nums: an array of integers containing n + 1 integers, where each integer is in range [1, n] inclusive

    Returns:
        repeated number (there is only one repeated number in nums)
    """
    # Floyd's cycle detection algorithm
    slow = fast = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    new = 0
    while True:
        new = nums[new]
        slow = nums[slow]
        if slow == new:
            return slow


if __name__ == "__main__":
    print(find_duplicate_number([1, 3, 4, 2, 2]))
    print(find_duplicate_number([3, 1, 3, 4, 2]))
    print(find_duplicate_number([1, 1]))
    print(find_duplicate_number([2, 2, 2, 2, 2]))
    print(find_duplicate_number([1, 4, 4, 2, 4]))
    print(find_duplicate_number([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]))
