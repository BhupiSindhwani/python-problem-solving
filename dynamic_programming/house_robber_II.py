from typing import List


def rob_util(nums):
    one, two = 0, 0
    for num in nums:
        temp = max(num + one, two)
        one, two = two, temp

    return two


def rob(nums: List[int]) -> int:
    """
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
    stashed. All houses at this place are arranged in a circle.

    That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system
    connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house,
    return the maximum amount of money you can rob tonight without alerting the police.

    Args:
        nums: an integer array representing the amount of money of each house

    Returns:
        the maximum amount of money you can rob tonight without alerting the police
    """
    if len(nums) == 1:
        return nums[0]

    return max(rob_util(nums[:-1]), rob_util(nums[1:]))


if __name__ == '__main__':
    print(rob([2, 3, 2]))
    print(rob([1, 2, 3, 1]))
    print(rob([1, 2, 3]))
    print(rob([4, 6, 2, 7, 2, 2, 9, 2]))
    print(rob([1]))
