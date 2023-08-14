from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Given the root of a binary tree, invert the tree, and return its root.

    Args:
        root: root of a binary tree

    Returns:
        root of the inverted tree
    """
    # use depth first traversal and swap left and right nodes

    if root:
        invert_binary_tree(root.left)
        invert_binary_tree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        # print(root.val, end=" ")

    return root


if __name__ == "__main__":
    tree_node = TreeNode(4)
    tree_node.left = TreeNode(2)
    tree_node.right = TreeNode(7)
    tree_node.left.left = TreeNode(1)
    tree_node.left.right = TreeNode(3)
    tree_node.right.left = TreeNode(6)
    tree_node.right.right = TreeNode(9)

    invert_binary_tree(tree_node)
