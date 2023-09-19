from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """
    Given an integer array nums of unique elements, return all possible subsets (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.

    Args:
        nums: an integer array of unique elements

    Returns:
        all possible subsets (the power set)
    """
    # # Initial Solution
    # output = [[]]
    # for num in nums:
    #     curr_elem_subsets = []
    #     for elem in output[1:]:
    #         new_elem = elem.copy()
    #         new_elem.append(num)
    #         curr_elem_subsets.append(new_elem)
    #     output.append([num])
    #     output.extend(curr_elem_subsets)
    #
    # return output

    # Solution using backtracking
    result = []

    curr_subset = []

    def dfs(i):
        if i >= len(nums):
            result.append(curr_subset.copy())
            return

        # decision to include nums[i]
        curr_subset.append(nums[i])
        dfs(i + 1)

        # decision to not include nums[i]
        curr_subset.pop()
        dfs(i + 1)

    dfs(0)
    return result


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
    print(subsets([0]))
