from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers
    such that they add up to target.

    You can return the answer in any order.
    Args:
        nums: array of integers
        target: integer target

    Returns:
        indices of the two numbers that add up to target
    """
    num_dict = {}
    for idx, num in enumerate(nums):
        pair = target - num
        if pair in num_dict:
            return [num_dict[pair], idx]
        num_dict[num] = idx


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))
