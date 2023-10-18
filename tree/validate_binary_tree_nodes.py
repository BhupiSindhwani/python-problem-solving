from typing import List


def validate_binary_tree_nodes(n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    """
    You have n binary tree nodes numbered from 0 to n - 1 where node_i has two children
    leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

    If node_i has no left child then leftChild[i] will equal -1, similarly for the right child.

    Note that the nodes have no values and that we only use the node numbers in this problem.

    Args:
        n: number of binary tree nodes
        leftChild: an integer array representing left child for nodes
        rightChild: an integer array representing right child for nodes

    Returns:
        true if all the given nodes form exactly one valid binary tree, otherwise false
    """
    # Create set of all child nodes and remove -1
    child_set = set(leftChild + rightChild)
    child_set.discard(-1)  # does not through an error if the value doesn't exist in set

    # Check if all the nodes are child nodes, return False
    if len(child_set) == n:
        return False

    # Find the root node
    root = -1
    for idx in range(n):
        if idx not in child_set:
            root = idx
            break

    visited_nodes = set()

    def dfs(node):
        if node == -1:
            return True
        if node in visited_nodes:
            return False
        visited_nodes.add(node)
        return dfs(leftChild[node]) and dfs(rightChild[node])

    return dfs(root) and len(visited_nodes) == n


if __name__ == '__main__':
    print(validate_binary_tree_nodes(4, [1, -1, 3, -1], [2, -1, -1, -1]))
    print(validate_binary_tree_nodes(4, [1, -1, 3, -1], [2, 3, -1, -1]))
    print(validate_binary_tree_nodes(2, [1, 0], [-1, -1]))
    print(validate_binary_tree_nodes(6, [1, -1, -1, 4, -1, -1], [2, -1, -1, 5, -1, -1]))
    print(validate_binary_tree_nodes(4, [3, -1, 1, -1], [-1, -1, 0, -1]))
