from collections import defaultdict
from typing import List


def majority_element(nums: List[int]) -> List[int]:
    """
    Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

    Args:
        nums: an integer array of size n

    Returns:
        list of elements that appear more than n/3 times
    """
    # # Solution using HashMap
    # result = []
    # n = len(nums)
    # nums_count = {}
    #
    # for num in nums:
    #     nums_count[num] = nums_count.get(num, 0) + 1
    #
    # for num in nums_count:
    #     if nums_count[num] > n // 3:
    #         result.append(num)
    #
    # return result

    # Solution with O(n) time complexity and O(1) space complexity
    result = []
    nums_count = defaultdict(int)

    for num in nums:
        nums_count[num] += 1
        if len(nums_count) > 2:
            new_nums_count = defaultdict(int)
            for n, c in nums_count.items():
                if c > 1:
                    new_nums_count[n] = c - 1
            nums_count = new_nums_count

    for key in nums_count:
        if nums.count(key) > len(nums) // 3:
            result.append(key)

    return result


if __name__ == "__main__":
    print(majority_element([3, 2, 3]))
    print(majority_element([1]))
    print(majority_element([1, 2]))
    print(majority_element([0, 3, 4, 0]))
    print(majority_element([3, 3, 1, 1, 1, 1, 2, 4, 4, 3, 3, 3, 4, 4]))
