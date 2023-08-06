from typing import List


def max_profit_stock(prices: List[int]) -> int:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and
    choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Args:
        prices: an array of prices

    Returns:
        max profit; otherwise 0 if there is no profit
    """
    if len(prices) < 2:
        return 0

    start, end = 0, 1

    max_profit = 0

    while end < len(prices):
        if prices[end] <= prices[start]:
            start = end
        max_profit = max(max_profit, prices[end] - prices[start])
        end += 1

    return max_profit


if __name__ == "__main__":
    print(max_profit_stock([7, 1, 5, 3, 6, 4]))
    print(max_profit_stock([7, 6, 4, 3, 1]))
    print(max_profit_stock([1, 2]))
    print(max_profit_stock([2, 1, 2, 1, 0, 1, 2]))
    print(max_profit_stock([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]))
