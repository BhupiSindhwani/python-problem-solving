from typing import List

# # Solution using naive recursion
# def find_knapsack(capacity: int, weights: List[int], values: List[int], n: int) -> int:
#     """
#     Args:
#         capacity: capacity target
#         weights: weights of items
#         values: values of items
#         n: number of items
#
#     Returns:
#         the maximum possible value to fit items in a knapsack with total capacity <= target capacity
#     """
#     # Base condition
#     if n == 0 or capacity == 0:
#         return 0
#
#     if weights[n-1] <= capacity:
#         return max(values[n-1] + find_knapsack(capacity - weights[n-1], weights, values, n-1),
#                    find_knapsack(capacity, weights, values, n-1))
#
#     return find_knapsack(capacity, weights, values, n-1)


# # Solution using top-down (with memoization) dynamic programming
# def find_knapsack(capacity: int, weights: List[int], values: List[int], n: int):
#     """
#     Args:
#         capacity: capacity target
#         weights: weights of items
#         values: values of items
#         n: number of items
#
#     Returns:
#         the maximum possible value to fit items in a knapsack with total capacity <= target capacity
#     """
#     dp = [[-1 for i in range(capacity + 1)] for j in range(n + 1)]
#     return find_knapsack_value(capacity, weights, values, n, dp)
#
#
# def find_knapsack_value(capacity, weights, values, n, dp) -> int:
#     if n == 0 or capacity == 0:
#         return 0
#
#     if dp[n][capacity] != -1:
#         return dp[n][capacity]
#
#     if weights[n-1] <= capacity:
#         dp[n][capacity] = max(values[n-1] + find_knapsack_value(capacity-weights[n-1], weights, values, n-1, dp),
#                               find_knapsack_value(capacity, weights, values, n-1, dp))
#         return dp[n][capacity]
#
#     dp[n][capacity] = find_knapsack_value(capacity, weights, values, n-1, dp)
#     return dp[n][capacity]

# # Solution using bottoms-up (tabulation) dynamic programming
def find_knapsack(capacity: int, weights: List[int], values: List[int], n: int) -> int:
    """
    Args:
        capacity: capacity target
        weights: weights of items
        values: values of items
        n: number of items

    Returns:
        the maximum possible value to fit items in a knapsack with total capacity <= target capacity
    """
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]


if __name__ == "__main__":
    weights = [[1, 2, 3, 5], [4], [2], [3, 6, 10, 7, 2], [3, 6, 10, 7, 2, 12, 15, 10, 13, 20]]
    values = [[1, 5, 4, 8], [2], [3], [12, 10, 15, 17, 13], [12, 10, 15, 17, 13, 12, 30, 15, 18, 20]]
    capacity = [6, 3, 3, 10, 20]
    n = [4, 1, 1, 5, 10]

    for i in range(len(values)):
        print(find_knapsack(capacity[i], weights[i], values[i], n[i]))
