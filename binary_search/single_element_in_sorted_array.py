from typing import List


def single_element_in_sorted_array(nums: List[int]) -> int:
    """
    You are given a sorted array consisting of only integers where every element appears exactly twice,
    except for one element which appears exactly once.

    Return the single element that appears only once.

    Your solution must run in O(log n) time and O(1) space.

    Args:
        nums: a sorted array of integers

    Returns:
        the single element that appears only once
    """
    if len(nums) == 1:
        return nums[0]

    left, right = 0, len(nums) - 1

    while left <= right:
        # mid = (left + right) // 2   # risk of overflow
        mid = left + ((right - left) // 2)
        if mid % 2 == 0:
            if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                right = mid - 1
            elif mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                left = mid + 1
            else:
                return nums[mid]
        elif mid % 2 == 1:
            if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                left = mid + 1
            elif mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                right = mid - 1
            else:
                return nums[mid]


if __name__ == "__main__":
    print(single_element_in_sorted_array([1, 1, 2, 3, 3, 4, 4, 8, 8]))
    print(single_element_in_sorted_array([3, 3, 7, 7, 10, 11, 11]))
    print(single_element_in_sorted_array([3]))
    print(single_element_in_sorted_array([3, 3]))
    print(single_element_in_sorted_array([1, 1, 2]))
