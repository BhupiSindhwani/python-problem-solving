from typing import List


def monotonic_array(nums: List[int]) -> bool:
    """
    An array is monotonic if it is either monotone increasing or monotone decreasing.
    An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
    An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

    Given an integer array nums, return true if the given array is monotonic, or false otherwise.

    Args:
        nums: an integer array

    Returns:
        true if the given array is monotonic, otherwise false
    """
    # increasing = False
    # decreasing = False
    #
    # for idx in range(1, len(nums)):
    #     if nums[idx] > nums[idx - 1]:
    #         if decreasing:
    #             return False
    #         else:
    #             increasing = True
    #     if nums[idx] < nums[idx - 1]:
    #         if increasing:
    #             return False
    #         else:
    #             decreasing = True
    #
    # return True

    increasing = False
    decreasing = False

    for idx in range(1, len(nums)):
        if nums[idx] > nums[idx - 1] and not increasing:
            increasing = True
        if nums[idx] < nums[idx - 1] and not decreasing:
            decreasing = True
        if increasing and decreasing:
            return False

    return True


if __name__ == "__main__":
    print(monotonic_array([1, 2, 2, 3]))
    print(monotonic_array([6, 5, 4, 4]))
    print(monotonic_array([1, 3, 2]))
    print(monotonic_array([1, 1]))
    print(monotonic_array([1]))
    print(monotonic_array([1, 9]))
