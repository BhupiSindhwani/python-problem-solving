from typing import List


def max_profit_stock_with_cooldown(prices: List[int]) -> int:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    Find the maximum profit you can achieve.
    You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times)
    with the following restrictions:

    - After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day)

    Note: You may not engage in multiple transactions simultaneously
    (i.e., you must sell the stock before you buy again).

    Args:
        prices: an array representing daily price of a given stock

    Returns:
        the maximum profit with one day cooldown restriction
    """
    dp = {}

    def dfs(i, state):
        if i >= len(prices):
            return 0

        if (i, state) in dp:
            return dp[(i, state)]

        cooldown = dfs(i + 1, state)
        if state == 'buy':
            buy = dfs(i + 1, 'sell') - prices[i]
            dp[(i, state)] = max(buy, cooldown)
        elif state == 'sell':
            sell = dfs(i + 2, 'buy') + prices[i]
            dp[(i, state)] = max(sell, cooldown)

        # print(dp)
        return dp[(i, state)]

    return dfs(0, 'buy')


if __name__ == '__main__':
    print(max_profit_stock_with_cooldown([1, 2, 3, 0, 2]))
    print(max_profit_stock_with_cooldown([1, 2, 3, 0, 8]))
    print(max_profit_stock_with_cooldown([0, 2, 3, 1, 8]))
    print(max_profit_stock_with_cooldown([1, 2, 3, 2, 8]))
    print(max_profit_stock_with_cooldown([1, 2, 3, 2, 0, 8]))
    print(max_profit_stock_with_cooldown([1, 2, 5, 0, 2]))
    print(max_profit_stock_with_cooldown([2, 1, 5, 0, 2]))
    print(max_profit_stock_with_cooldown([1]))
