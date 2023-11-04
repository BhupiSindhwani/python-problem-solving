import collections
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional['Node']) -> Optional['Node']:
    """
    Given a reference of a node in a connected undirected graph.

    Return a deep copy (clone) of the graph.

    Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

    Args:
        node: a reference of a node in a connected undirected graph

    Returns:
        a deep copy (clone) of the graph
    """
    visited = {}
    queue = collections.deque()
    if node:
        new_node = Node(val=node.val, neighbors=node.neighbors.copy())
        visited[new_node.val] = new_node
    else:
        new_node = None
    queue.append(new_node)

    while queue:
        curr_node = queue.popleft()
        if curr_node:
            for idx in range(len(curr_node.neighbors)):
                curr_neighbor = curr_node.neighbors[idx]
                if curr_neighbor.val not in visited:
                    temp_node = Node(val=curr_neighbor.val, neighbors=curr_neighbor.neighbors.copy())
                    visited[curr_neighbor.val] = temp_node
                    curr_node.neighbors[idx] = temp_node
                    queue.append(temp_node)
                else:
                    curr_node.neighbors[idx] = visited[curr_neighbor.val]

    return new_node


if __name__ == '__main__':
    # adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
    # print(clone_graph(Node(1, [2, 4])))
    pass
