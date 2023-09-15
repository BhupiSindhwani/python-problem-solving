from typing import List


def spiral_matrix(matrix: List[List[int]]) -> List[int]:
    """
    Given an m x n matrix, return all elements of the matrix in spiral order.

    Args:
        matrix: an m x n matrix

    Returns:
        a list of all elements of the input matrix in spiral order
    """
    output = []

    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])

    while top < bottom and left < right:

        # traverse from left to right
        for i in range(left, right):
            output.append(matrix[top][i])
        top += 1

        # traverse from top to bottom
        for j in range(top, bottom):
            output.append(matrix[j][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # traverse from right to left
        for i in range(right - 1, left - 1, -1):
            output.append(matrix[bottom - 1][i])
        bottom -= 1

        # traverse from bottom to top
        for j in range(bottom - 1, top - 1, -1):
            output.append(matrix[j][left])
        left += 1

    return output


if __name__ == "__main__":
    print(spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(spiral_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print(spiral_matrix([[6, 9, 7]]))
