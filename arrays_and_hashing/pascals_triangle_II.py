from typing import List


def pascals_triangle_row(rowIndex: int) -> List[int]:
    """
    Given an integer rowIndex, return the rowIndex-th (0-indexed) row of the Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly.

    Args:
        rowIndex: an integer

    Returns:
        the rowIndex-th (0-indexed) row of the Pascal's triangle
    """
    output_row = [1]

    for num in range(1, rowIndex + 1):
        prev = 0
        for idx in range(len(output_row)):
            temp = output_row[idx]
            output_row[idx] += prev
            prev = temp
        output_row.append(prev)

    return output_row


if __name__ == '__main__':
    print(pascals_triangle_row(3))
    print(pascals_triangle_row(0))
    print(pascals_triangle_row(1))
