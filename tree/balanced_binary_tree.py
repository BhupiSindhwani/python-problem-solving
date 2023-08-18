from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_binary_tree(root: Optional[TreeNode]) -> None:
    if root:
        print_binary_tree(root.left)
        print_binary_tree(root.right)
        print(root.val, end=" ")


def balanced_binary_tree(root: Optional[TreeNode]) -> bool:
    """
    Given a binary tree, determine if it is height-balanced

    Args:
        root: root of a binary tree

    Returns:
        true if the tree is height-balanced, otherwise false
    """
    is_balanced = True

    def depth(node: Optional[TreeNode]) -> int:
        nonlocal is_balanced
        if node:
            left = depth(node.left)
            right = depth(node.right)
            if abs(left - right) > 1:
                is_balanced = False
            return 1 + max(left, right)
        else:
            return 0

    depth(root)

    return is_balanced


if __name__ == "__main__":
    tree_node = TreeNode(1)
    tree_node.left = TreeNode(2)
    tree_node.right = TreeNode(2)
    tree_node.left.left = TreeNode(3)
    tree_node.left.right = TreeNode(3)
    tree_node.left.left.left = TreeNode(4)
    tree_node.left.left.right = TreeNode(4)

    print_binary_tree(tree_node)
    print()
    print(balanced_binary_tree(tree_node))
