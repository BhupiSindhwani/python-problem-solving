from collections import defaultdict
from typing import List


def restore_array_from_adjacent_pairs(adjacentPairs: List[List[int]]) -> List[int]:
    """
    There is an integer array nums that consists of n unique elements, but you have forgotten it.
    However, you do remember every pair of adjacent elements in nums.

    You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that
    the elements ui and vi are adjacent in nums.

    It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs,
    either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

    Return the original array nums. If there are multiple solutions, return any of them.

    Args:
        adjacentPairs: a 2D integer array of size n - 1 where adjacentPairs[i] = [ui, vi] indicates adjacent in nums

    Returns:
        the original array nums
    """
    result = []
    visited = set()

    # Build adjacency map
    adj_map = defaultdict(set)

    for p1, p2 in adjacentPairs:
        adj_map[p1].add(p2)
        adj_map[p2].add(p1)

    # Identify a starting node
    start_node = 0
    for key, val in adj_map.items():
        if len(val) == 1:
            start_node = key

    # # Using recursive traversal
    # def dfs(node: int) -> None:
    #     if node not in visited:
    #         visited.add(node)
    #         result.append(node)
    #         for neighbor in adj_map[node]:
    #             dfs(neighbor)
    #
    # # Traverse the graph and append to result
    # dfs(start_node)

    # Using queue iteratively
    queue = [start_node]
    while queue:
        curr_node = queue.pop()
        if curr_node not in visited:
            visited.add(curr_node)
            result.append(curr_node)
            for neighbor in adj_map[curr_node]:
                queue.append(neighbor)

    # return the result
    return result


if __name__ == '__main__':
    print(restore_array_from_adjacent_pairs([[2, 1], [3, 4], [3, 2]]))
    print(restore_array_from_adjacent_pairs([[4, -2], [1, 4], [-3, 1]]))
    print(restore_array_from_adjacent_pairs([[100000, -100000]]))


# 1: 2
# 2: 1, 3
# 3: 4, 2
# 4: 3
#

# 4: -2, 1
# -2: 4
# 1: 4, -3
# -3: 1


# 4 - -2
# | - -3
# 1