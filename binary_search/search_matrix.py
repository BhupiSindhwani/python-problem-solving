from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    You are given an m x n integer matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.
    Given an integer target, return true if target is in matrix or false otherwise.

    You must write a solution in O(log(m * n)) time complexity.

    Args:
        matrix: m x n integer matrix
        target: target integer

    Returns:
        true if target is in matrix, otherwise false
    """
    n_row, n_col = len(matrix), len(matrix[0])
    left, right = 0, (n_row * n_col) - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // n_col
        col = mid % n_col
        if target > matrix[row][col]:
            left = mid + 1
        elif target < matrix[row][col]:
            right = mid - 1
        else:
            return True

    return False


if __name__ == "__main__":
    print(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
    print(search_matrix([[1, 1]], 2))
