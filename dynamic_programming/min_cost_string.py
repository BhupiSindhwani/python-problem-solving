from typing import List


def min_cost_string(n: int, cost: List[List[int]]) -> int:
    """
    You can only use characters - A, B, C and D to form a string of length n
    You are also given a 2-D integer array with cost of each position to use the character

    You cannot have 2 consecutive positions with the same character

    Calculate the smallest cost to make a string of length n

    Args:
        n: an integer representing the length of string
        cost: a 2-D integer array with cost of each position to use the character

    Returns:
        the smallest cost to make a string of length n
    """
    dp = {}

    def helper(prev_letter, curr_ix):
        if (prev_letter, curr_ix) in dp:
            return dp[(prev_letter, curr_ix)]

        if curr_ix == n:
            return 0

        min_cost = float('inf')
        for letter in range(4):
            if letter != prev_letter:
                remaining_cost = cost[curr_ix][letter] + helper(letter, curr_ix + 1)
                min_cost = min(min_cost, remaining_cost)

        dp[(prev_letter, curr_ix)] = min_cost
        # print(dp)
        return dp[(prev_letter, curr_ix)]

    return helper(-1, 0)


if __name__ == '__main__':
    print(min_cost_string(2, [[2, 3, 4, 5], [7, 3, 4, 1]]))     # 3
    print(min_cost_string(2, [[2, 3, 4, 3], [1, 3, 4, 4]]))     # 4
    print(min_cost_string(2, [[3, 2, 4, 5], [7, 3, 4, 1]]))     # 3
    print(min_cost_string(3, [[2, 3, 4, 5], [7, 3, 4, 1], [1, 2, 9, 2]]))    # 4
    print(min_cost_string(3, [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]))    # 4
