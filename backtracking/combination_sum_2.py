from typing import List


def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]:
    """
    Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations
    in candidates where the candidate numbers sum to target.

    Each number in candidates may only be used once in the combination.

    Note: The solution set must not contain duplicate combinations.

    Args:
        candidates: an array of candidate numbers
        target: a target number

    Returns:
        all unique combinations in candidates where the candidate numbers sum to target
    """
    # # Initial Solution
    # candidates.sort()
    # result = []
    #
    # def backtrack(i, curr, total):
    #     if total == target:
    #         result.append(curr.copy())
    #         return
    #
    #     if i >= len(candidates) or total > target:
    #         return
    #
    #     # include candidates[i]
    #     curr.append(candidates[i])
    #     backtrack(i + 1, curr, total + candidates[i])
    #
    #     # not include candidates[i]
    #     curr.pop()
    #     while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
    #         i += 1
    #     backtrack(i + 1, curr, total)
    #
    # backtrack(0, [], 0)
    # return result

    candidates.sort()
    res = []

    def backtrack(cur, pos, target):
        if target == 0:
            res.append(cur.copy())
            return
        if target <= 0:
            return

        prev = -1
        for i in range(pos, len(candidates)):
            if candidates[i] == prev:
                continue
            cur.append(candidates[i])
            backtrack(cur, i + 1, target - candidates[i])
            cur.pop()
            prev = candidates[i]

    backtrack([], 0, target)
    return res


if __name__ == "__main__":
    print(combination_sum_2([10, 1, 2, 7, 6, 1, 5], 8))
    print(combination_sum_2([2, 5, 2, 1, 2], 5))
