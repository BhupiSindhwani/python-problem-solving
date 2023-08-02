from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if
    every element is distinct.

    Args:
        nums: integer array

    Returns:
        true if any value appears at least twice in nums, otherwise false
    """
    unique_nums = set()
    for num in nums:
        if num in unique_nums:
            return True
        else:
            unique_nums.add(num)
    return False


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))
    print(contains_duplicate([1, 2, 3, 4]))
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
