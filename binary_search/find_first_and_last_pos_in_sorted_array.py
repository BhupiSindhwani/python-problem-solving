from typing import List


def find_first_and_last_pos_in_sorted_array(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums sorted in non-decreasing order,
    find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.

    Args:
        nums: an array of integers sorted in non-decreasing order
        target: an integer target value

    Returns:
        list of starting and ending position of a given target value
    """
    result = [-1, -1]
    left, right = 0, len(nums) - 1
    idx = -1

    # def bin_search(nums, target, left_idx, right_idx, idx, result, pos ='first'):
    #     while left_idx <= right_idx:
    #         mid = (left_idx + right_idx) // 2
    #         if nums[mid] < target:
    #             left_idx = mid + 1
    #         elif nums[mid] > target:
    #             right_idx = mid - 1
    #         else:
    #             if pos == 'first':
    #                 idx = mid
    #                 if mid - 1 >= 0 and nums[mid - 1] == target:
    #                     right_idx = mid - 1
    #                 else:
    #                     result[0] = mid
    #                     result[1] = mid
    #                     return idx
    #             elif pos == 'last':
    #                 if mid + 1 < len(nums) and nums[mid + 1] == target:
    #                     left_idx = mid + 1
    #                 else:
    #                     result[1] = mid
    #                     return idx
    #     return idx

    # find the first pos
    # idx = bin_search(nums, target, left, right, idx, result, 'first')
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            idx = mid
            if mid - 1 >= 0 and nums[mid - 1] == target:
                right = mid - 1
            else:
                result[0] = mid
                result[1] = mid
                break

    if idx == -1:
        return result

    left, right = idx + 1, len(nums) - 1
    # find the last pos
    # idx = bin_search(nums, target, left, right, idx, result, 'last')
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            if mid + 1 < len(nums) and nums[mid + 1] == target:
                left = mid + 1
            else:
                result[1] = mid
                break

    return result


if __name__ == "__main__":
    print(find_first_and_last_pos_in_sorted_array([5, 7, 7, 8, 8, 10], 8))
    print(find_first_and_last_pos_in_sorted_array([5, 7, 8, 8, 8, 10], 8))
    print(find_first_and_last_pos_in_sorted_array([5, 8, 8, 8, 8, 10], 8))
    print(find_first_and_last_pos_in_sorted_array([5, 8, 8, 8, 8, 8], 8))
    print(find_first_and_last_pos_in_sorted_array([5, 8, 8], 8))
    print(find_first_and_last_pos_in_sorted_array([5, 7, 7, 8, 8, 10], 6))
    print(find_first_and_last_pos_in_sorted_array([], 0))
    print(find_first_and_last_pos_in_sorted_array([1], 1))
