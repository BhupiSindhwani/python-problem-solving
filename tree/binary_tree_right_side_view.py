from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_right_side_view(root: Optional[TreeNode]) -> List[int]:
    """
    Given the root of a binary tree, imagine yourself standing on the right side of it,
    return the values of the nodes you can see ordered from top to bottom.

    Args:
        root: root of a binary tree

    Returns:
        the values of the nodes on the right side of the tree ordered from top to bottom
    """
    queue = deque()
    result = []

    if root:
        queue.append([root])

    while queue:
        nodes = queue.popleft()
        last_node = nodes[-1]
        result.append(last_node.val)
        curr_level_nodes = []
        for node in nodes:
            if node.left:
                curr_level_nodes.append(node.left)
            if node.right:
                curr_level_nodes.append(node.right)
        if curr_level_nodes:
            queue.append(curr_level_nodes)

    return result


if __name__ == "__main__":
    tree_node = TreeNode(1)
    tree_node.left = TreeNode(2)
    tree_node.right = TreeNode(3)
    tree_node.left.left = TreeNode(4)
    # tree_node.left.right = TreeNode(5)
    # tree_node.right.right = TreeNode(4)
    print(binary_tree_right_side_view(tree_node))
    print(binary_tree_right_side_view(None))
