from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).

    Args:
        root: root of a binary tree

    Returns:
        list of level order traversal of the tree's node's values
    """
    output = []
    queue = deque()
    if root:
        queue.append(root)

    while queue:
        values = []
        for _ in range(len(queue)):
            node = queue.popleft()
            values.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        output.append(values)

    return output


if __name__ == "__main__":
    tree_node = TreeNode(3)
    tree_node.left = TreeNode(9)
    tree_node.right = TreeNode(20)
    tree_node.right.left = TreeNode(15)
    tree_node.right.right = TreeNode(7)

    print(binary_tree_level_order_traversal(tree_node))

    tree_node = TreeNode(1)
    tree_node.left = TreeNode(2)
    tree_node.right = TreeNode(3)
    tree_node.left.left = TreeNode(4)
    tree_node.right.right = TreeNode(5)

    print(binary_tree_level_order_traversal(tree_node))
