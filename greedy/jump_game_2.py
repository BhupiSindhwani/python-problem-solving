from typing import List


def jump_game_2(nums: List[int]) -> int:
    """
    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

    Each element nums[i] represents the maximum length of a forward jump from index i.
    In other words, if you are at nums[i], you can jump to any nums[i + j] where:

        0 <= j <= nums[i] and
        i + j < n

    Return the minimum number of jumps to reach nums[n - 1].
    The test cases are generated such that you can reach nums[n - 1].

    Args:
        nums: 0-indexed array of integers of length n

    Returns:
        the minimum number of jumps to reach nums[n-1]
    """
    jumps, left, right = 0, 0, 0

    while right < len(nums) - 1:
        window_end = 0
        for idx in range(left, right + 1):
            window_end = max(window_end, idx + nums[idx])
        left = right + 1
        right = window_end
        jumps += 1

    return jumps


if __name__ == "__main__":
    print(jump_game_2([2, 3, 1, 1, 4]))
    print(jump_game_2([2, 3, 0, 1, 4]))
