import heapq
from typing import List, Dict


def shortest_path(n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
    # build adj list for nodes
    adj_list = [[] for _ in range(n)]
    for sr, dt, wt in edges:
        adj_list[sr].append((dt, wt))

    print(adj_list)

    # initialize every node weight as -1 (weight of unreachable node)
    node_map = {i: -1 for i in range(n)}

    # start with the source and identify the lowest weighted neighbor
    min_heap = [(0, src)]  # initialize min heap with distance from src node and node itself
    while min_heap:
        prev_wt, prev_node = heapq.heappop(min_heap)
        if node_map[prev_node] == -1:
            node_map[prev_node] = prev_wt

            for curr_node, curr_wt in adj_list[prev_node]:
                if node_map[curr_node] == -1:
                    heapq.heappush(min_heap, (prev_wt + curr_wt, curr_node))

    return node_map


if __name__ == '__main__':
    print(shortest_path(5, [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4], [2, 3, 8], [2, 4, 2], [3, 4, 5]], 0))
