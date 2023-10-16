from typing import List


def pascals_triangle(numRows: int) -> List[List[int]]:
    """
    Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it

    Args:
        numRows: an integer

    Returns:
        the first numRows of Pascal's triangle
    """
    result = [[1]]

    for num in range(1, numRows):
        prev = 0
        curr_row = []
        for curr in result[-1]:
            curr_row.append(prev + curr)
            prev = curr
        curr_row.append(prev)
        result.append(curr_row)

    return result


if __name__ == '__main__':
    print(pascals_triangle(5))
    print(pascals_triangle(1))
