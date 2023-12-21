from typing import List


def max_width_of_vertical_area(points: List[List[int]]) -> int:

    # Solution using sorting
    points.sort(key=lambda x: x[0])
    max_len = 0
    x_prev = points[0][0]

    for x, y in points[1:]:
        max_len = max(max_len, x - x_prev)
        x_prev = x

    return max_len


if __name__ == '__main__':
    print(max_width_of_vertical_area([[8, 7], [9, 9], [7, 4], [9, 7]]))
    print(max_width_of_vertical_area([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
