from typing import List


def jump_game(nums: List[int]) -> bool:
    """
    You are given an integer array nums. You are initially positioned at the array's first index,
    and each element in the array represents your maximum jump length at that position.

    Return true if you can reach the last index, or false otherwise.

    Args:
        nums: an integer array representing your max jump length at each position

    Returns:
        true if you can reach the last index, otherwise false
    """
    target_idx = len(nums) - 1

    for idx in range(len(nums) - 1, -1, -1):
        if idx + nums[idx] >= target_idx:
            target_idx = idx

    if target_idx == 0:
        return True

    return False


if __name__ == "__main__":
    print(jump_game([2, 3, 1, 1, 4]))
    print(jump_game([3, 2, 1, 0, 4]))
    print(jump_game([0]))
    print(jump_game([2, 5, 0, 0]))
    print(jump_game([3, 0, 8, 2, 0, 0, 1]))
    print(jump_game([0, 2, 3]))
