import collections
from typing import List


def max_area_island(grid: List[List[int]]) -> int:
    """
    You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected
    4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

    The area of an island is the number of cells with a value 1 on the island.

    Return the maximum area of an island in grid. If there is no island, return 0.

    Args:
        grid: m x n binary matrix

    Returns:
        the maximum area of an island in grid; if there is no island, return 0
    """
    # Solution using BFS iteratively
    m, n = len(grid), len(grid[0])
    num_islands = 0
    max_area = 0
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def valid_traversal(x, y):
        nonlocal max_area, num_islands
        curr_area = 0
        if grid[x][y] == 1:
            queue = collections.deque()
            queue.append((x, y))
            visited.add((x, y))
            curr_area += 1
            while queue:
                r, c = queue.popleft()
                for rd, cd in directions:
                    curr_r, curr_c = r + rd, c + cd
                    if 0 <= curr_r < m and \
                            0 <= curr_c < n and \
                            grid[curr_r][curr_c] == 1 and \
                            (curr_r, curr_c) not in visited:
                        queue.append((curr_r, curr_c))
                        visited.add((curr_r, curr_c))
                        curr_area += 1
            num_islands += 1
            max_area = max(max_area, curr_area)

    for row in range(m):
        for col in range(n):
            if (row, col) not in visited:
                valid_traversal(row, col)

    return max_area

    # # Solution using DFS recursively
    # m, n = len(grid), len(grid[0])
    # num_islands = 0
    # max_area = 0
    # visited = set()
    # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    #
    # def dfs(r, c) -> int:
    #     curr_area = 0
    #     if grid[r][c] == 1:
    #         visited.add((r, c))
    #         curr_area += 1
    #         for rd, cd in directions:
    #             curr_r, curr_d = r + rd, c + cd
    #             if 0 <= curr_r < m and \
    #                     0 <= curr_d < n and \
    #                     (curr_r, curr_d) not in visited:
    #                 curr_area += dfs(curr_r, curr_d)
    #     return curr_area
    #
    # for row in range(m):
    #     for col in range(n):
    #         if (row, col) not in visited:
    #             max_area = max(max_area, dfs(row, col))
    #
    # return max_area

    # # Recursive way to count the number of islands
    # def dfs(r, c) -> int:
    #     if grid[r][c] == 1:
    #         visited.add((r, c))
    #         for rd, cd in directions:
    #             curr_r, curr_d = r + rd, c + cd
    #             if 0 <= curr_r < m and \
    #                     0 <= curr_d < n and \
    #                     (curr_r, curr_d) not in visited:
    #                 dfs(curr_r, curr_d)
    #         return True
    #     return False
    #
    # for row in range(m):
    #     for col in range(n):
    #         if (row, col) not in visited:
    #             num_islands += 1 if dfs(row, col) else 0
    #
    # return num_islands


if __name__ == '__main__':
    input_grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                  [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(max_area_island(input_grid))

    input_grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    print(max_area_island(input_grid))

    input_grid = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    print(max_area_island(input_grid))
