from typing import List


def container_with_most_water(height: List[int]) -> int:
    """
    You are given an integer array height of length n.
    There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Args:
        height: an integer array of length n

    Returns:
        maximum amount of water a container can store
    """
    left, right = 0, len(height) - 1

    max_area = 0

    while left < right:
        # if left > 0 and height[left] < height[left - 1]:
        #     left += 1
        #     continue
        # if right < len(height) - 1 and height[right] < height[right + 1]:
        #     right -= 1
        #     continue
        curr_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, curr_area)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return max_area


if __name__ == "__main__":
    print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(container_with_most_water([1, 1]))
