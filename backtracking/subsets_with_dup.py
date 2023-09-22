from typing import List


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    """
    Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.

    Args:
        nums: an integer array that may contain duplicates

    Returns:
        all possible subsets (the power se) without duplicate subsets
    """
    result = []
    nums.sort()

    def backtrack(i, curr_subset):
        if i >= len(nums):
            result.append(curr_subset.copy())
            return

        # decision to select nums[i]
        curr_subset.append(nums[i])
        backtrack(i + 1, curr_subset)

        # decision to not select nums[i]
        curr_subset.pop()
        while i + 1 < len(nums) and nums[i + 1] == nums[i]:
            i += 1
        backtrack(i + 1, curr_subset)

    backtrack(0, [])
    return result


if __name__ == "__main__":
    print(subsets_with_dup([1, 2, 3]))
    print(subsets_with_dup([1, 2, 2]))
    print(subsets_with_dup([0]))
