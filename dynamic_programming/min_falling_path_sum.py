from typing import List


def min_falling_path_sum(matrix: List[List[int]]) -> int:
    """
    Given an n x n array of integers matrix, return the minimum sum of any falling path
    through matrix.

    A falling path starts at any element in the first row and chooses the element in the
    next row that is either directly below or diagonally left/right.

    Specifically, the next element from position (row, col) will be
    (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

    Args:
        matrix: m x n array of integers

    Returns:
        the minimum sum of any falling path through matrix
    """
    m, n = len(matrix), len(matrix[0])
    cache = {}  # (row, col) -> min cost from that position

    for col_idx in range(n):
        cache[(m - 1, col_idx)] = matrix[m - 1][col_idx]

    def backtrack(row, col):

        # base condition to check in cache
        if (row, col) in cache:
            return cache[(row, col)]

        # print(f"row: {row}, col: {col}")

        # check for out of bounds
        if 0 <= row < m and 0 <= col < n:

            # check for the three possible options
            down_left, down, down_right = float('inf'), float('inf'), float('inf')

            if row + 1 < m and col - 1 >= 0:
                down_left = backtrack(row + 1, col - 1)

            if row + 1 < m:
                down = backtrack(row + 1, col)

            if row + 1 < m and col + 1 < n:
                down_right = backtrack(row + 1, col + 1)

            cache[(row, col)] = matrix[row][col] + min(down_left, down, down_right)
            # print(cache)
            return cache[(row, col)]

    for c in range(n):
        backtrack(0, c)

    min_cost = cache[(0, 0)]
    for col in range(n):
        min_cost = min(min_cost, cache[(0, col)])

    return min_cost


if __name__ == '__main__':
    print(min_falling_path_sum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
    print(min_falling_path_sum([[-19, 57], [-40, -5]]))
