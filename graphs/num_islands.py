import collections
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """
    Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
    return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    You may assume all four edges of the grid are all surrounded by water.

    Args:
        grid: m x n 2D binary grid representing a map of land ("1"s) and water ("0"s)

    Returns:
        the number of islands
    """
    m, n = len(grid), len(grid[0])
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    islands_count = 0

    def valid_traversal(r, c):
        nonlocal islands_count
        if grid[r][c] == '1':
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                x, y = queue.popleft()
                for xd, yd in directions:
                    curr_xd, curr_yd = x + xd, y + yd
                    if 0 <= curr_xd < m and \
                            0 <= curr_yd < n and \
                            grid[curr_xd][curr_yd] == '1' and \
                            (curr_xd, curr_yd) not in visited:
                        queue.append((curr_xd, curr_yd))
                        visited.add((curr_xd, curr_yd))
            islands_count += 1

    for row in range(m):
        for col in range(n):
            if (row, col) not in visited:
                # print((row, col))
                # print(visited)
                valid_traversal(row, col)

    return islands_count


def num_islands_including_diagonal(grid: List[List[str]]) -> int:
    """
    Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
    return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally, vertically or diagonally.
    You may assume all four edges of the grid are all surrounded by water.

    Args:
        grid: m x n 2D binary grid representing a map of land ("1"s) and water ("0"s)

    Returns:
        the number of islands
    """
    m, n = len(grid), len(grid[0])
    visited = set()
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    islands_count = 0

    def valid_traversal(r, c):
        nonlocal islands_count
        if grid[r][c] == '1':
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                x, y = queue.popleft()
                for xd, yd in directions:
                    curr_xd, curr_yd = x + xd, y + yd
                    if 0 <= curr_xd < m and \
                            0 <= curr_yd < n and \
                            grid[curr_xd][curr_yd] == '1' and \
                            (curr_xd, curr_yd) not in visited:
                        queue.append((curr_xd, curr_yd))
                        visited.add((curr_xd, curr_yd))
            islands_count += 1

    for row in range(m):
        for col in range(n):
            if (row, col) not in visited:
                # print((row, col))
                # print(visited)
                valid_traversal(row, col)

    return islands_count


if __name__ == '__main__':
    input_grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(num_islands(input_grid))
    print(num_islands_including_diagonal(input_grid))

    input_grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(num_islands(input_grid))
    print(num_islands_including_diagonal(input_grid))
