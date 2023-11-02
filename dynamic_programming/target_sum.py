from typing import List


def target_sum(nums: List[int], target: int) -> int:
    """
    You are given an integer array nums and an integer target.

    You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums
    and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the
    expression "+2-1".

    Return the number of different expressions that you can build, which evaluates to target.

    Args:
        nums: an integer array
        target: an integer target

    Returns:
        the number of different expressions that you can build, which evaluates to target
    """
    dp = {}

    def backtrack(idx: int, prev_val: int) -> int:
        # print(f"idx: {idx}; prev_val: {prev_val}")

        if idx == len(nums):
            return 1 if prev_val == target else 0

        if (idx, prev_val) in dp:
            return dp[(idx, prev_val)]

        num_idx = nums[idx]

        # + choice
        positive_choice = backtrack(idx + 1, prev_val + num_idx)

        # - choice
        negative_choice = backtrack(idx + 1, prev_val - num_idx)

        dp[(idx, prev_val)] = positive_choice + negative_choice
        return dp[(idx, prev_val)]

    return backtrack(0, 0)


if __name__ == '__main__':
    print(target_sum([1, 1, 1, 1, 1], 3))
    print(target_sum([1], 1))
    print(target_sum([1, 2], 1))
    print(target_sum([1, 0], 1))
    print(target_sum([47, 23, 35, 27, 30, 42, 26, 42, 30, 6, 8, 48, 44, 38, 41, 50, 18, 19, 19, 5], 40))
