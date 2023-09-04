from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: Optional[TreeNode]) -> int:
    """
    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge
    connecting them. A node can only appear in the sequence at most once.
    Note that the path does not need to pass through the root.

    The path sum of a path is the sum of the node's values in the path.

    Given the root of a binary tree, return the maximum path sum of any non-empty path.

    Args:
        root: root of a binary tree

    Returns:
        maximum path sum of any non-empty path of the given binary tree
    """
    max_sum = root.val

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal max_sum
        if node:
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            max_sum = max(max_sum, node.val + left + right)
            return node.val + max(left, right)
        else:
            return 0

    dfs(root)
    return max_sum


def bfs_traversal(node: Optional[TreeNode]) -> None:
    queue = deque()
    queue.append(node)
    while queue:
        curr = queue.popleft()
        print(f"{curr.val}->", end="")
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)


if __name__ == "__main__":
    tree_node = TreeNode(-10)
    tree_node.left = TreeNode(9)
    tree_node.right = TreeNode(20)
    tree_node.right.left = TreeNode(15)
    tree_node.right.right = TreeNode(7)
    bfs_traversal(tree_node)
    print()
    print(max_path_sum(tree_node))

    tree_node = TreeNode(-3)
    bfs_traversal(tree_node)
    print()
    print(max_path_sum(tree_node))

    tree_node = TreeNode(-2)
    tree_node.left = TreeNode(-1)
    bfs_traversal(tree_node)
    print()
    print(max_path_sum(tree_node))
