def climbing_stairs(n: int) -> int:
    """
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Args:
        n: an integer representing number of steps to reach the top

    Returns:
        the distinct number of ways to climb to the top (each time you can either climb 1 or 2 steps)
    """
    # # Solution using dynamic programming using hash map
    # dp = {1: 1,
    #       2: 2}
    #
    # for num in range(3, n + 1):
    #     dp[num] = dp[num - 1] + dp[num - 2]
    #
    # return dp[n]

    # Solution using dynamic programming using an array
    # if n == 1:
    #     return 1
    #
    # dp = [0] * n
    # dp[0] = 1
    # dp[1] = 2
    #
    # for num in range(2, n):
    #     dp[num] = dp[num - 1] + dp[num - 2]
    #
    # return dp[n - 1]

    # # Solution using dynamic programming with two variables
    # if n == 1:
    #     return 1
    #
    # one, two = 1, 2
    #
    # for num in range(3, n + 1):
    #     new = one + two
    #     one, two = two, new
    #
    # return two

    # Solution using dynamic programming with memoization
    cache = {n: 1}  # curr_steps -> num_combinations

    def backtrack(curr_steps):

        # base condition
        if curr_steps > n:
            return 0

        if curr_steps in cache:
            return cache[curr_steps]

        # 1 step
        one_step = backtrack(curr_steps + 1)

        # 2 step
        two_step = backtrack(curr_steps + 2)

        cache[curr_steps] = one_step + two_step
        return cache[curr_steps]

    return backtrack(0)


if __name__ == "__main__":
    print(climbing_stairs(2))
    print(climbing_stairs(3))
