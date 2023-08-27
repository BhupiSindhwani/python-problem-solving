from typing import List


def gas_station(gas: List[int], cost: List[int]) -> int:
    """
    There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

    You have a car with an unlimited gas tank, and it costs: costs[i] of gas to travel from the ith station
    to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

    Given two integer arrays gas and cost, return the starting gas station's index if you can travel around
    the circuit once in the clockwise direction, otherwise return -1.

    If there exists a solution, it is guaranteed to be unique

    Args:
        gas: an integer array representing the amount of gas at the n stations along a circular route
        cost: an integer array representing the cost of gas to travel from one station to the next

    Returns:
        the starting gas station's index if you can travel around the circuit once clockwise, otherwise -1
    """
    # # Initial Solution
    # n = len(gas)
    # idx, res_idx = 0, -1
    # curr_gas = 0
    # second_loop = False
    #
    # while idx < n:
    #     if idx == res_idx:
    #         break
    #     g = curr_gas + gas[idx] - cost[idx]
    #     if g >= 0:
    #         if res_idx == -1:
    #             res_idx = idx
    #         curr_gas = g
    #     else:
    #         curr_gas = 0
    #         res_idx = -1
    #         if second_loop:
    #             break
    #     if idx == n - 1 and res_idx != -1:
    #         idx = -1
    #         second_loop = True
    #     idx += 1
    # return res_idx

    # Optimized Solution
    n = len(gas)
    res_idx = -1
    curr_gas, total_gas = 0, 0

    for idx in range(n):
        total_gas += gas[idx] - cost[idx]
        curr_gas += gas[idx] - cost[idx]

        if curr_gas < 0:
            curr_gas = 0
            res_idx = -1
        else:
            if res_idx == -1:
                res_idx = idx

    return res_idx if total_gas >= 0 else -1


if __name__ == "__main__":
    print(gas_station([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(gas_station([2, 3, 4], [3, 4, 3]))
