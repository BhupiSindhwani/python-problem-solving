from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Given an array of distinct integers candidates and a target integer target, return a list of all unique
    combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
    frequency of at least one of the chosen numbers is different.

    Args:
        candidates: an array of distinct integers candidates
        target: an integer target

    Returns:
        a list of all unique combinations of candidates where the chosen numbers sum to target
    """
    result = []

    def dfs(i, curr, total):
        if total == target:
            result.append(curr.copy())
            return

        if i >= len(candidates) or total > target:
            return

        # decision to add candidate element
        curr.append(candidates[i])
        dfs(i, curr, total + candidates[i])

        # decision to not include candidate element
        curr.pop()
        dfs(i + 1, curr, total)

    dfs(0, [], 0)
    return result


if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], 7))
    print(combination_sum([2, 3, 5], 8))
    print(combination_sum([2], 1))
