from collections import deque
from typing import List


def surrounded_regions(board: List[List[str]]) -> None:
    """
    Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in that surrounded region.

    Args:
        board: m x n matrix board containing 'X' and 'O'

    Returns:
        None
    """
    # rows, cols = len(board), len(board[0])
    #
    # def dfs(r, c):
    #     if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
    #         return
    #     board[r][c] = '-'
    #     dfs(r, c + 1)
    #     dfs(r + 1, c)
    #     dfs(r, c - 1)
    #     dfs(r - 1, c)
    #
    # for row in range(rows):
    #     for col in range(cols):
    #         if board[row][col] == 'O' and (row in (0, rows - 1) or col in (0, cols - 1)):
    #             dfs(row, col)
    #
    # for row in range(rows):
    #     for col in range(cols):
    #         if board[row][col] == 'O':
    #             board[row][col] = 'X'
    #         if board[row][col] == '-':
    #             board[row][col] = 'O'

    # Solution using iterative loop
    m, n = len(board), len(board[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    # num_islands = 0
    queue = deque()

    def valid_traversal(r, c):
        # nonlocal num_islands
        if (r, c) not in visited:
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                x, y = queue.popleft()
                board[x][y] = '-'
                for xd, yd in directions:
                    curr_x, curr_y = x + xd, y + yd
                    if 0 < curr_x < m - 1 and \
                            0 < curr_y < n - 1 and \
                            (curr_x, curr_y) not in visited and \
                            board[curr_x][curr_y] == 'O':
                        board[curr_x][curr_y] = '-'
                        queue.append((curr_x, curr_y))
                        visited.add((curr_x, curr_y))

            # num_islands += 1

    for row in range(m):
        for col in range(n):
            if board[row][col] == 'O' and (row in (0, m - 1) or col in (0, n - 1)):
                valid_traversal(row, col)

    for row in range(m):
        for col in range(n):
            if board[row][col] == 'O':
                board[row][col] = 'X'
            if board[row][col] == '-':
                board[row][col] = 'O'


if __name__ == '__main__':
    input_board = [["X", "X", "X", "X"],
                   ["X", "O", "O", "X"],
                   ["X", "X", "O", "X"],
                   ["X", "O", "X", "X"]]
    print(input_board)
    surrounded_regions(input_board)
    print(input_board)

    input_board = [["X", "X", "X", "X"],
                   ["X", "O", "O", "X"],
                   ["X", "X", "O", "X"],
                   ["X", "O", "0", "X"]]
    print(input_board)
    surrounded_regions(input_board)
    print(input_board)

    input_board = [["0", "X", "X", "X"],
                   ["X", "O", "O", "X"],
                   ["X", "X", "O", "X"],
                   ["X", "O", "X", "X"]]
    print(input_board)
    surrounded_regions(input_board)
    print(input_board)

    input_board = [["O", "X", "X", "O", "X"],
                   ["X", "O", "O", "X", "O"],
                   ["X", "O", "X", "O", "X"],
                   ["O", "X", "O", "O", "O"],
                   ["X", "X", "O", "X", "O"]]
    print(input_board)
    surrounded_regions(input_board)
    print(input_board)
