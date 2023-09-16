from typing import List


def set_matrix_zeroes(matrix: List[List[int]]) -> None:
    """
    Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.

    You must do it in place.

    Args:
        matrix: an m x n integer matrix

    Returns:
        None
    """
    # # Initial Solution
    # top, bottom = 0, len(matrix)
    # left, right = 0, len(matrix[0])
    # lu_indexes = set()
    # rd_indexes = set()
    #
    # while top < bottom:
    #
    #     for i in range(left, right):
    #         if matrix[top][i] == 0:
    #             # add left indexes
    #             for _ in range(i):
    #                 lu_indexes.add((top, _))
    #
    #             # add up indexes
    #             for _ in range(top):
    #                 lu_indexes.add((_, i))
    #
    #             # add right indexes
    #             for _ in range(i + 1, right):
    #                 rd_indexes.add((top, _))
    #
    #             # add down indexes
    #             for _ in range(top + 1, bottom):
    #                 rd_indexes.add((_, i))
    #
    #     top += 1
    #
    # for x, y in lu_indexes.union(rd_indexes):
    #     matrix[x][y] = 0

    # # Revised Solution with space complexity O(m + n)
    # top, bottom = 0, len(matrix)
    # left, right = 0, len(matrix[0])
    # col_indexes = [0] * right
    # row_indexes = [0] * bottom
    #
    # while top < bottom:
    #
    #     for i in range(left, right):
    #         if matrix[top][i] == 0:
    #             # add col indexes
    #             col_indexes[i] = 1
    #
    #             # add row indexes
    #             row_indexes[top] = 1
    #
    #     top += 1
    #
    # for x in range(bottom):
    #     for y in range(right):
    #         if row_indexes[x] or col_indexes[y]:
    #             matrix[x][y] = 0

    # Revised Solution with space complexity O(1)
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])
    row_zero = False

    while top < bottom:

        for i in range(left, right):
            if matrix[top][i] == 0:
                # add col indexes
                matrix[0][i] = 0

                # add row indexes
                if top > 0:
                    matrix[top][0] = 0
                else:
                    row_zero = True

        top += 1

    # zero elements except the first row and column
    for x in range(1, bottom):
        for y in range(1, right):
            if matrix[0][y] == 0 or matrix[x][0] == 0:
                matrix[x][y] = 0

    # zero the first col if required
    if matrix[0][0] == 0:
        for x in range(bottom):
            matrix[x][0] = 0

    # zero the first row if required
    if row_zero:
        for y in range(right):
            matrix[0][y] = 0


if __name__ == "__main__":
    mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_matrix_zeroes(mat)
    print(mat)

    mat = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_matrix_zeroes(mat)
    print(mat)
