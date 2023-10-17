from typing import List


def remove_duplicates_from_sorted_array(nums: List[int]) -> int:
    """
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each
    unique element appears only once.

    The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were
    present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.

    Args:
        nums: an integer array sorted in non-decreasing order

    Returns:
        the size of first k elements of nums that contain the unique elements in the original order
    """
    left, right = 0, 0

    while right < len(nums):
        if nums[right] > nums[left]:
            left += 1
            # nums[left], nums[right] = nums[right], nums[left]
            nums[left] = nums[right]
        right += 1

    # print(nums)
    return left + 1


if __name__ == '__main__':
    print(remove_duplicates_from_sorted_array([1, 1, 2]))
    print(remove_duplicates_from_sorted_array([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
