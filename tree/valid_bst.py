from typing import Optional, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def valid_bst(root: Optional[TreeNode]) -> bool:
    """
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:

    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.

    Args:
        root: root of a binary tree

    Returns:
        true if valid binary search tree (BST), otherwise false
    """

    def dfs(node: Optional[TreeNode],
            min_val: Union[int, float] = float('-inf'),
            max_val: Union[int, float] = float('inf')) -> bool:
        if node:
            # print(f"node: {node.val}; range: {min_val} - {max_val}")
            if node.val <= min_val or node.val >= max_val:
                return False

            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)
        return True

    return dfs(root)


if __name__ == "__main__":
    tree_node = TreeNode(5)
    tree_node.left = TreeNode(1)
    tree_node.right = TreeNode(6)
    tree_node.right.left = TreeNode(3)
    tree_node.right.right = TreeNode(7)

    # tree_node = TreeNode(2)
    # tree_node.left = TreeNode(2)
    # tree_node.right = TreeNode(2)

    # tree_node = TreeNode(3)
    # tree_node.left = TreeNode(1)
    # tree_node.right = TreeNode(5)
    # tree_node.left.left = TreeNode(0)
    # tree_node.left.right = TreeNode(2)
    # tree_node.right.left = TreeNode(4)
    # tree_node.right.right = TreeNode(6)

    print(valid_bst(tree_node))
