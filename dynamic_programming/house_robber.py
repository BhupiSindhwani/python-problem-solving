from typing import List


def rob(nums: List[int]) -> int:
    """
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of
    money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have
    security systems connected, and it will automatically contact the police if two adjacent houses were broken
    into on the same night.

    Given an integer array nums representing the amount of money of each house,
    return the maximum amount of money you can rob tonight without alerting the police.

    Args:
        nums: an integer array representing the amount tof money of each house

    Returns:
        the maximum amount of money you can rob tonight without alerting the police
    """
    # # Naive recursion
    # if len(nums) == 1:
    #     return nums[0]
    # elif len(nums) == 2:
    #     return max(nums[0], nums[1])
    #
    # return max(nums[0] + rob(nums[2:]), rob(nums[1:]))

    # Solution using dynamic programming
    one, two = 0, 0
    for num in nums:
        temp = max(num + one, two)
        one, two = two, temp
    return two


if __name__ == '__main__':
    print(rob([1, 2, 3, 1]))
    print(rob([2, 7, 9, 3, 1]))
    print(rob([4, 6, 2, 7, 2, 2, 9, 2]))
