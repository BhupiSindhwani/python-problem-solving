from typing import List


def search_rotated_sorted_array(nums: List[int], target: int) -> int:
    """
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
    such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

    Args:
        nums: an array of unique elements of length n sorted in ascending order & rotated
        target: target integer

    Returns:
        the index of target in the nums array, otherwise -1
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[left]:
            # sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # non-sored
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    print(search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0))
    print(search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3))
    print(search_rotated_sorted_array([1], 0))
    print(search_rotated_sorted_array([1, 3], 3))
    print(search_rotated_sorted_array([3, 1], 1))
    print(search_rotated_sorted_array([3, 5, 1], 3))
