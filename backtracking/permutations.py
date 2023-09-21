from typing import List


def permutations(nums: List[int]) -> List[List[int]]:
    """
    Given an array nums of distinct integers, return all the possible permutations.
    You can return the answer in any order.

    Args:
        nums: an array of distinct integers

    Returns:
        list of all the possible permutations
    """
    res = []

    # base case
    if len(nums) == 1:
        return [nums[:]]  # nums[:] is a deep copy

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permutations(nums)

        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res


if __name__ == "__main__":
    print(permutations([1, 2, 3]))
    print(permutations([0, 1]))
    print(permutations([1]))
