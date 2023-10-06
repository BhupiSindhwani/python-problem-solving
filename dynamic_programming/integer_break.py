def integer_break(n: int) -> int:
    """
    Given an integer n, break it into the sum of k positive integers, where k >= 2,
    and maximize the product of those integers.

    Return the maximum product you can get.

    Args:
        n: an integer

    Returns:
        the maximum product by breaking it into the sum of k positive integers, where k >=2
    """
    # # Solution using recursion & caching
    # dp = {1: 1}
    #
    # def dfs(num):
    #     if num in dp:
    #         return dp[num]
    #
    #     dp[num] = 0 if num == n else num
    #     for i in range(1, num):
    #         val = dfs(i) * dfs(num - i)
    #         dp[num] = max(dp[num], val)
    #     return dp[num]
    #
    # return dfs(n)

    # Solution using dynamic programming
    dp = {1: 1}

    for num in range(2, n + 1):
        dp[num] = 0 if num == n else num
        for i in range(1, num):
            val = dp[i] * dp[num - i]
            dp[num] = max(dp[num], val)

    return dp[n]


if __name__ == "__main__":
    print(integer_break(2))
    print(integer_break(10))
