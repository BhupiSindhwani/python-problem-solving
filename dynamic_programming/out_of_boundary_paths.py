def out_of_boundary_paths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    """
    There is an m x n grid with a ball. The ball is initially at the position
    [startRow, startColumn].

    You are allowed to move the ball to one of the four adjacent cells in the grid
    (possibly out of the grid crossing the grid boundary).

    You can apply at most maxMove moves to the ball.

    Given the five integers m, n, maxMove, startRow, startColumn,
    return the number of paths to move the ball out of the grid boundary.

    Since the answer can be very large, return it modulo 109 + 7.

    Args:
        m: number of rows in the grid
        n: number of cols in the grid
        maxMove: maximum number of moves
        startRow: starting Row
        startColumn: starting Col

    Returns:
        the number of paths to move the ball out of the grid boundary
    """
    cache = {}  # (row, col, moves) -> num of paths
    mod = 10 ** 9 + 7

    def backtrack(row, col, moves):

        if 0 <= row < m and 0 <= col < n:

            if moves == 0:
                return 0

            if (row, col, moves) in cache:
                return cache[(row, col, moves)]

            cache[(row, col, moves)] = (
                       (backtrack(row, col - 1, moves - 1) +
                        backtrack(row + 1, col, moves - 1)) % mod +
                       (backtrack(row, col + 1, moves - 1) +
                        backtrack(row - 1, col, moves - 1)) % mod
               ) % mod

            return cache[(row, col, moves)]
        else:
            return 1

    return backtrack(startRow, startColumn, maxMove)


if __name__ == '__main__':
    print(out_of_boundary_paths(2, 2, 2, 0, 0))
    print(out_of_boundary_paths(1, 3, 3, 0, 1))
