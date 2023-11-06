import collections
from typing import List


def pacific_atlantic_water_flow(heights: List[List[int]]) -> List[List[int]]:
    """
    There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
    The Pacific Ocean touches the island's left and top edges, and
    the Atlantic Ocean touches the island's right and bottom edges.

    The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where
    heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

    The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east,
    and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from
    any cell adjacent to an ocean into the ocean.

    Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from
    cell (ri, ci) to both the Pacific and Atlantic oceans.

    Args:
        heights: m x n grid representing a rectangular island with corresponding height of each cell

    Returns:
        a 2D list of grid coordinates result where result[i] = [ri, ci] denotes the rain water can flow into oceans
    """
    # # Initial Solution
    # m, n = len(heights), len(heights[0])
    # visited = {}
    # result = []
    # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    #
    # def valid_traversal(x, y):
    #     if (x, y) in visited:
    #         return visited[(x, y)]
    #
    #     pacific, atlantic = False, False
    #     queue = collections.deque()
    #     queue.append((x, y))
    #     curr_set = set()
    #
    #     while queue:
    #         # print(queue)
    #         r, c = queue.popleft()
    #         if (r, c) in visited:
    #             p, a = visited[(r, c)]
    #             pacific, atlantic = pacific or p, atlantic or a
    #             if pacific and atlantic:
    #                 break
    #         else:
    #             curr_set.add((r, c))
    #             print(queue)
    #             print(curr_set)
    #             for rd, cd in directions:
    #                 curr_r, curr_c = r + rd, c + cd
    #                 if curr_r < 0 or curr_c < 0:
    #                     pacific = True
    #                 if curr_r == m or curr_c == n:
    #                     atlantic = True
    #                 if 0 <= curr_r < m and \
    #                         0 <= curr_c < n and \
    #                         (curr_r, curr_c) not in curr_set and \
    #                         heights[curr_r][curr_c] <= heights[r][c]:
    #                     queue.append((curr_r, curr_c))
    #     #         print(f"pacific: {pacific}, atlantic: {atlantic}")
    #     # print(f"x: {x}, y: {y}")
    #     # print(f"pacific: {pacific}, atlantic: {atlantic}")
    #     # print(visited)
    #     visited[(x, y)] = (pacific, atlantic)
    #     if pacific and atlantic:
    #         result.append((x, y))
    #
    # for row in range(m):
    #     for col in range(n):
    #         if (row, col) not in visited:
    #             valid_traversal(row, col)
    #
    # return result

    rows, cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()
    result = []

    def dfs(x, y, visit, prev_height):
        if (x, y) in visit or x < 0 or y < 0 or x >= rows or y >= cols or heights[x][y] < prev_height:
            return
        visit.add((x, y))
        dfs(x, y + 1, visit, heights[x][y])
        dfs(x + 1, y, visit, heights[x][y])
        dfs(x, y - 1, visit, heights[x][y])
        dfs(x - 1, y, visit, heights[x][y])

    for col in range(cols):
        dfs(0, col, pacific, heights[0][col])
        dfs(rows - 1, col, atlantic, heights[rows - 1][col])

    for row in range(rows):
        dfs(row, 0, pacific, heights[row][0])
        dfs(row, cols - 1, atlantic, heights[row][cols - 1])

    for r in range(rows):
        for c in range(cols):
            if (r, c) in pacific and (r, c) in atlantic:
                result.append([r, c])

    return result


if __name__ == '__main__':
    input_heights = [[1, 2, 2, 3, 5],
                     [3, 2, 3, 4, 4],
                     [2, 4, 5, 3, 1],
                     [6, 7, 1, 4, 5],
                     [5, 1, 1, 2, 4]]
    print(pacific_atlantic_water_flow(input_heights))

    # input_heights = [[1, 2],
    #                  [1, 1]]
    # input_heights = [[1, 2],
    #                  [1, 0]]
    input_heights = [[1, 5, 4],
                     [4, 4, 3]]
    # input_heights = [[1, 1]]
    print(pacific_atlantic_water_flow(input_heights))
