from typing import List


def trap_rain_water(height: List[int]) -> int:
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it can trap after raining.

    Args:
        height: an integer array of non-negative numbers

    Returns:
        how much water can trap after raining
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    max_left, max_right = height[left], height[right]

    total_area = 0

    while left < right:
        if height[left] <= height[right]:
            left += 1
            max_left = max(max_left, height[left])
            total_area += max(min(max_left, max_right) - height[left], 0)
        else:
            right -= 1
            max_right = max(max_right, height[right])
            total_area += max(min(max_left, max_right) - height[right], 0)

    return total_area


if __name__ == "__main__":
    print(trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(trap_rain_water([4, 2, 0, 3, 2, 5]))
    print(trap_rain_water([4, 2]))
    print(trap_rain_water([]))

# [4,2,0,3,2,5]
#            _
#  _        | |
# | |    _  | |
# | |_  | |_| |
# | | | | | | |
# |_|_|_|_|_|_|
#
