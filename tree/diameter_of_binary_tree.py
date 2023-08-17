from typing import Optional, List


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


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    Given the root of a binary tree, return the length of the diameter of the tree.

    The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    This path may or may not pass through the root.

    The length of a path between two nodes is represented by the number of edges between them.

    Args:
        root: root of a binary tree

    Returns:
        the diameter of the binary tree
    """
    max_diameter = 0

    def count_elements(root: Optional[TreeNode]) -> int:
        nonlocal max_diameter

        if root:
            left_count = count_elements(root.left)
            right_count = count_elements(root.right)
            curr_diameter = left_count + right_count
            max_diameter = max(max_diameter, curr_diameter)
            depth = 1 + max(left_count, right_count)
            return depth
        else:
            return 0

    count_elements(root)

    return max_diameter


if __name__ == "__main__":
    tree_node = TreeNode(1)
    tree_node.left = TreeNode(2)
    tree_node.right = TreeNode(3)
    tree_node.left.left = TreeNode(4)
    tree_node.left.right = TreeNode(5)

    print_binary_tree(tree_node)
    print()
    print(diameter_of_binary_tree(tree_node))
