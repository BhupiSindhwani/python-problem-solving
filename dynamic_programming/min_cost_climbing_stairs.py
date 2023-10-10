from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    """
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
    Once you pay the cost, you can either climb one or two steps.

    You can either start from the step with index 0, or the step with index 1.

    Return the minimum cost to reach the top of the floor.

    Args:
        cost: an integer array where cost[i] is the cost of ith step on a staircase

    Returns:
        the minimum cost to reach the top of the floor
    """
    # # Solution building from end to start
    # dp_one, dp_two = cost[-2], cost[-1]
    #
    # for cost_num in cost[-3::-1]:
    #     curr_min_cost = min(dp_two + cost_num, dp_one + cost_num)
    #     dp_two = dp_one
    #     dp_one = curr_min_cost
    #
    # return min(dp_one, dp_two)

    # Solution building from start to end
    dp_one, dp_two = cost[0], cost[1]

    for cost_num in cost[2:]:
        curr_min_cost = min(dp_two + cost_num, dp_one + cost_num)
        dp_one, dp_two = dp_two, curr_min_cost

    return min(dp_one, dp_two)


if __name__ == "__main__":
    print(min_cost_climbing_stairs([10, 15, 20]))
    print(min_cost_climbing_stairs([10, 15]))
    print(min_cost_climbing_stairs([15, 10]))
    print(min_cost_climbing_stairs([10, 15, 20, 25]))
    print(min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
