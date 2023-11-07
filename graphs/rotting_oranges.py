import collections
from typing import List


def rotting_oranges(grid: List[List[int]]) -> int:
    """
    You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange.
    If this is impossible, return -1.

    Args:
        grid: m x n grid representing a cell with three options - empty, fresh orange, or rotten orange

    Returns:
        the minimum number of minutes until no cell has a fresh orange; if not possible, return -1
    """
    rows, cols = len(grid), len(grid[0])
    minutes, fresh_oranges = 0, 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = collections.deque()

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                fresh_oranges += 1
            if grid[row][col] == 2:
                queue.append((row, col))

    while queue and fresh_oranges > 0:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for rd, cd in directions:
                curr_r, curr_c = r + rd, c + cd
                if curr_r < 0 or curr_c < 0 or curr_r >= rows or curr_c >= cols or grid[curr_r][curr_c] != 1:
                    continue
                grid[curr_r][curr_c] = 2
                queue.append((curr_r, curr_c))
                fresh_oranges -= 1
        minutes += 1

    return minutes if not fresh_oranges else -1


if __name__ == '__main__':
    input_grid = [[2, 1, 1],
                  [1, 1, 0],
                  [0, 1, 1]]
    print(rotting_oranges(input_grid))

    input_grid = [[2, 1, 1],
                  [0, 1, 1],
                  [1, 0, 1]]
    print(rotting_oranges(input_grid))

    input_grid = [[1, 1, 1],
                  [1, 2, 1],
                  [1, 1, 1]]
    print(rotting_oranges(input_grid))

    input_grid = [[1, 0, 1],
                  [0, 2, 1],
                  [1, 1, 1]]
    print(rotting_oranges(input_grid))

    input_grid = [[0, 2]]
    print(rotting_oranges(input_grid))

    input_grid = [[2, 1, 1],
                  [1, 1, 1],
                  [0, 1, 2]]
    print(rotting_oranges(input_grid))
