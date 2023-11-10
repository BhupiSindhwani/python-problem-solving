from typing import List


def number_or_provinces(isConnected: List[List[int]]) -> int:
    """
    There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
    and city b is connected directly with city c, then city a is connected indirectly with city c.

    A province is a group of directly or indirectly connected cities and no other cities outside the group.

    You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly
    connected, and isConnected[i][j] = 0 otherwise.

    Return the total number of provinces.

    Args:
        isConnected: an n x n matrix where isConnected[i][j] = 1 if the ith and the jth city are directly connected

    Returns:
        the total number of provinces
    """
    n = len(isConnected)
    parent = [i for i in range(n)]
    rank = [1] * n

    def find(node):
        par = parent[node]
        while par != parent[par]:
            parent[par] = parent[parent[par]]
            par = parent[par]
        return par

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return 0

        if rank[p1] >= rank[p2]:
            parent[p2] = parent[p1]
            rank[p1] += rank[p2]
        else:
            parent[p1] = parent[p2]
            rank[p2] += rank[p1]
        return 1

    num_provinces = n
    for row in range(n):
        for col in range(row + 1, n):
            if isConnected[row][col]:
                num_provinces -= union(row, col)

    return num_provinces


if __name__ == '__main__':
    print(number_or_provinces([[1, 1, 0],
                               [1, 1, 0],
                               [0, 0, 1]]))
    print(number_or_provinces([[1, 0, 0],
                               [0, 1, 0],
                               [0, 0, 1]]))
    print(number_or_provinces([[1, 1, 0, 1, 0],
                               [1, 1, 0, 0, 0],
                               [0, 0, 1, 0, 1],
                               [1, 0, 0, 1, 0],
                               [0, 0, 1, 0, 1]]))
