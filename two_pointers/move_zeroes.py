from typing import List


def move_zeroes(nums: List[int]) -> None:
    """
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the
    non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Args:
        nums: an integer array

    Returns:
        None
    """
    # # Initial Solution
    # left = 0
    #
    # while left < len(nums):
    #     if nums[left] == 0:
    #         break
    #     left += 1
    #
    # if left == len(nums):
    #     return
    #
    # right = left + 1
    # while left < right < len(nums):
    #     if nums[right] != 0:
    #         nums[left], nums[right] = nums[right], nums[left]
    #     while nums[left] != 0:
    #         left += 1
    #         if left == len(nums):
    #             return
    #     right += 1

    # Refactored Solution
    left, right = 0, 0

    for right in range(len(nums)):
        if nums[right] != 0 and nums[left] == 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        if nums[left] != 0:
            left += 1


if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    move_zeroes(arr)
    print(arr)

    arr = [5, 0, 1, 0, 3, 12]
    move_zeroes(arr)
    print(arr)

    arr = [5, 8, 1, 9, 3, 12]
    move_zeroes(arr)
    print(arr)

    arr = [0]
    move_zeroes(arr)
    print(arr)
