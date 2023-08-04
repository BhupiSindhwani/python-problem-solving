from typing import List


def two_sum_sorted_array(numbers: List[int], target: int) -> List[int]:
    """
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
    find two numbers such that they add up to a specific target number.

    Return the indices of the two numbers, index1 and index2,
    added by one as an integer array [index1, index2] of length 2.

    Args:
        numbers: 1-indexed sorted array of integers in non-decreasing order
        target: target number

    Returns:
        an array of length 2 with the indices of the two numbers that adds up to target number
    """
    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            return [left + 1, right + 1]
    return []


if __name__ == "__main__":
    print(two_sum_sorted_array([2, 7, 11, 15], 9))
    print(two_sum_sorted_array([2, 7, 11, 15], 26))
    print(two_sum_sorted_array([2, 3, 4], 6))
    print(two_sum_sorted_array([-1, 0], -1))
