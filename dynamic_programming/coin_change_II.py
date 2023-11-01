from typing import List, Set


def coin_change(amount: int, coins: List[int]) -> int:
    """
    You are given an integer array coins representing coins of different denominations and an integer amount
    representing a total amount of money.

    Return the number of combinations that make up that amount.
    If that amount of money cannot be made up by any combination of the coins, return 0.

    You may assume that you have an infinite number of each kind of coin.

    Args:
        amount: an integer representing a total amount of money
        coins: an integer array representing coins of different denominations

    Returns:
        the number of combinations that make up that amount; otherwise 0
    """
    # # Recursive Solution with memoization - O(n x M)
    # dp = {}
    #
    # def dfs(idx, target):
    #     if target == amount:
    #         return 1
    #     if target > amount:
    #         return 0
    #     if idx == len(coins):
    #         return 0
    #     if (idx, target) in dp:
    #         return dp[(idx, target)]
    #
    #     dp[(idx, target)] = dfs(idx, target + coins[idx]) + dfs(idx + 1, target)
    #     return dp[(idx, target)]
    #
    # return dfs(0, 0)

    # Dynamic Programming Solution - O(n x M)
    dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
    dp[0] = [1] * (len(coins) + 1)

    for target in range(1, amount + 1):
        for idx in range(len(coins) - 1, -1, -1):
            dp[target][idx] = dp[target][idx + 1]
            if target - coins[idx] >= 0:
                dp[target][idx] += dp[target - coins[idx]][idx]
    return dp[amount][0]


if __name__ == '__main__':
    print(coin_change(3, [1, 2]))
    print(coin_change(5, [1, 2, 5]))
    print(coin_change(3, [2]))
    print(coin_change(10, [10]))
