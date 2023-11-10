from collections import defaultdict
from typing import List


def redundant_connection(edges: List[List[int]]) -> List[int]:
    """
    In this problem, a tree is an undirected graph that is connected and has no cycles.

    You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
    The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.

    The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge
    between nodes ai and bi in the graph.

    Return an edge that can be removed so that the resulting graph is a tree of n nodes.
    If there are multiple answers, return the answer that occurs last in the input.

    Args:
        edges: an array representing edges of a graph

    Returns:
        an edge that can be removed so that the resulting graph is a tree of n nodes; return last edge more than one
    """
    parent = [n for n in range(len(edges) + 1)]
    rank = [1 for n in range(len(edges) + 1)]

    # Implement using union-find
    def find(node):
        par = parent[node]
        while par != parent[par]:
            parent[par] = parent[parent[par]]  # path compression
            par = parent[par]
        return par

    def union(node1, node2):
        parent1, parent2 = find(node1), find(node2)
        if parent1 == parent2:
            return False

        if rank[parent1] >= rank[parent2]:
            parent[parent2] = parent1
            rank[parent1] += rank[parent2]
        else:
            parent[parent1] = parent2
            rank[parent2] += rank[parent1]
        return True

    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]


if __name__ == '__main__':
    print(redundant_connection([[1, 2], [1, 3], [2, 3]]))
    print(redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
    print(redundant_connection([[2, 3], [3, 4], [1, 2], [1, 4], [1, 5]]))
    print(redundant_connection([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]))
    print(redundant_connection([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]))
    print(redundant_connection([[1, 5], [3, 4], [3, 5], [4, 5], [2, 4]]))
