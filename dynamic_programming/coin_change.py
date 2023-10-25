from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """
    You are given an integer array coins representing coins of different denominations and an integer amount
    representing a total amount of money.

    Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be
    made up by any combination of the coins, return -1.

    You may assume that you have an infinite number of each kind of coin.

    Args:
        coins: an integer array representing coins of different denominations
        amount: an integer representing a total amount of money

    Returns:
        the fewest number of coins to make up the given amount; otherwise return -1
    """
    dp = [0] + ([amount + 1] * amount)
    for target in range(1, len(dp)):
        for coin in coins:
            if target - coin >= 0:
                dp[target] = min(dp[target], 1 + dp[target - coin])

    # print(dp)
    return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == '__main__':
    print(coin_change([1, 2, 5], 11))
    print(coin_change([2], 3))
    print(coin_change([1], 0))
