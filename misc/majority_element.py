from typing import List


def majority_element(nums: List[int]) -> int:
    """
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.

    Args:
        nums: an integer array

    Returns:
        the majority element
    """
    # # Naive solution using linear time and linear space
    # nums_count = {}
    # max_count_key, max_count = 0, 0
    #
    # for num in nums:
    #     nums_count[num] = nums_count.get(num, 0) + 1
    #     if nums_count[num] > max_count:
    #         max_count = nums_count[num]
    #         max_count_key = num
    #
    # return max_count_key

    # Solution using Boyer Moore Majority Voting algorithm
    result, count = 0, 0

    for num in nums:
        if count == 0:
            result = num
        count += (1 if num == result else -1)

    return result


if __name__ == '__main__':
    print(majority_element([3, 2, 3]))
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))
