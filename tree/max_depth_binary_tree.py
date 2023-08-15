from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_binary_tree(root: Optional[TreeNode]) -> int:
    """
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the root node
    down to the farthest leaf node.

    Args:
        root: root of a binary tree

    Returns:
        maximum depth of the tree
    """
    # Initial Solution
    # def pre_order_traversal_depth(node: Optional[TreeNode], depth: int) -> int:
    #
    #     if node:
    #         depth += 1
    #         left_depth = pre_order_traversal_depth(node.left, depth)
    #         right_depth = pre_order_traversal_depth(node.right, depth)
    #         return max(left_depth, right_depth)
    #     else:
    #         return depth
    #
    # max_depth = 0
    # return max(max_depth, pre_order_traversal_depth(root, max_depth))

    # Other Solution
    if not root:
        return 0

    return 1 + max(max_depth_binary_tree(root.left), max_depth_binary_tree(root.right))


if __name__ == "__main__":
    tree_node = TreeNode(3)
    tree_node.left = TreeNode(9)
    tree_node.right = TreeNode(20)
    tree_node.right.left = TreeNode(15)
    tree_node.right.right = TreeNode(7)
    print(max_depth_binary_tree(tree_node))
