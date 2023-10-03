import math
from typing import List


def num_of_good_pairs(nums: List[int]) -> int:
    """
    Given an array of integers nums, return the number of good pairs.

    A pair (i, j) is called good if nums[i] == nums[j] and i < j.

    Args:
        nums: an integer array

    Returns:
        the number of good pairs
    """
    # # Initial solution using math.comb
    # num_good_pairs = 0
    # num_count = Counter(nums)
    # for key in num_count:
    #     num_good_pairs += math.comb(num_count[key], 2)
    # return num_good_pairs

    # Solution using without math.comb
    num_of_good_pairs = 0
    num_count = {}

    for num in nums:
        if num in num_count:
            num_of_good_pairs += num_count[num]
            num_count[num] += 1
        else:
            num_count[num] = 1

    return num_of_good_pairs


if __name__ == "__main__":
    print(num_of_good_pairs([1, 2, 3, 1, 1, 3]))
    print(num_of_good_pairs([1, 1, 1, 1]))
    print(num_of_good_pairs([1, 2, 3]))
