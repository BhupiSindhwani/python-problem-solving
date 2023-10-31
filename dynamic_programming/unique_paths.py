def unique_paths(m: int, n: int) -> int:
    """
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).

    The robot can only move either down or right at any point in time.

    Given the two integers m and n, return the number of possible unique paths that the robot can take to
    reach the bottom-right corner.

    Args:
        m: number of rows in the grid
        n: number of columns in the grid

    Returns:
        the number of possible unique paths that the robot can take to reach the bottom-right corner
    """
    # Solution using Time: O(m x n) and Space: O(m x n)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    dp[m - 1][n - 1] = 1

    for row in range(m - 1, -1, -1):
        for col in range(n - 1, -1, -1):
            if row == m - 1 and col == n - 1:
                continue
            dp[row][col] = dp[row][col + 1] + dp[row + 1][col]

    return dp[0][0]

    # # Solution using Time: O(m x n) and Space: O(n)
    # row = [1] * n
    #
    # for i in range(m - 1):
    #     new_row = [1] * n
    #     for j in range(n - 2, -1, -1):
    #         new_row[j] = new_row[j + 1] + row[j]
    #     row = new_row
    #
    # return row[0]


if __name__ == '__main__':
    print(unique_paths(3, 7))
    print(unique_paths(3, 2))
