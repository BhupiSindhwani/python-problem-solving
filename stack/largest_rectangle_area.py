from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    """
    Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
    return the area of the largest rectangle in the histogram.

    Args:
        heights: an array of integers heights

    Returns:
        the area of the largest rectangle in the histogram
    """
    stack = []
    max_area = 0

    for idx, height in enumerate(heights):
        i = idx

        while stack and stack[-1][0] > height:
            h, i = stack.pop()
            max_area = max(max_area, h * (idx - i))

        stack.append((height, i))

    while stack:
        max_area = max(max_area, stack[-1][0] * (len(heights) - stack[-1][-1]))
        stack.pop()

    return max_area


if __name__ == "__main__":
    print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))
    print(largest_rectangle_area([2, 1, 5, 6, 2, 3, 1, 1, 1, 1, 1, 1]))
    print(largest_rectangle_area([2, 4]))
    print(largest_rectangle_area([1, 2, 3, 4, 5]))
