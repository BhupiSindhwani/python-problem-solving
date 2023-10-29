from typing import List


def partition_equal_subset_sum(nums: List[int]) -> bool:
    """
    Given an integer array nums, return true if you can partition the array into two subsets such that the
    sum of the elements in both subsets is equal or false otherwise.

    Args:
        nums: an integer array

    Returns:
        true if the input array can be partitioned into two subsets with sum of elements in subsets are equal
    """
    sum_nums = sum(nums)

    if sum_nums % 2 != 0:
        return False

    target = sum_nums // 2
    possible_targets = set()

    for num in nums:
        for pt in possible_targets.copy():
            if pt + num <= target:
                possible_targets.add(pt + num)
                if pt + num == target:
                    return True
        possible_targets.add(num)
        if num == target:
            return True

    return True if target in possible_targets else False


if __name__ == '__main__':
    print(partition_equal_subset_sum([1, 5, 11, 5]))
    print(partition_equal_subset_sum([1, 5, 12]))
    print(partition_equal_subset_sum([1, 2, 3, 5]))
    print(partition_equal_subset_sum([2, 2, 1, 1]))
    print(partition_equal_subset_sum([1, 2, 3, 4, 5, 6, 7]))
