import collections
from typing import List


def valid_sudoku(board: List[List[str]]) -> bool:
    """
    Determine if a 9 x 9 Sudoku board is valid.
    Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

    Args:
        board: array of arrays representing a 9 x 9 Sudoku board

    Returns:
        true if the Sudoku board is valid, otherwise false
    """
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    boxes = collections.defaultdict(set)

    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                continue
            if board[row][col] in rows[row] or \
                    board[row][col] in cols[col] or \
                    board[row][col] in boxes[row//3, col//3]:
                return False
            rows[row].add(board[row][col])
            cols[col].add(board[row][col])
            boxes[(row // 3, col // 3)].add(board[row][col])

    return True


if __name__ == "__main__":
    print(valid_sudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                        [".", "9", "8", ".", ".", ".", ".", "6", "."],
                        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                        [".", "6", ".", ".", ".", ".", "2", "8", "."],
                        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

    print(valid_sudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
                        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                        [".", "9", "8", ".", ".", ".", ".", "6", "."],
                        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                        [".", "6", ".", ".", ".", ".", "2", "8", "."],
                        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
