from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

    Args:
        p: root of a binary tree
        q: root of a binary tree

    Returns:
        True if the two input binary trees are the same, otherwise False
    """
    if p and q:
        if p.val != q.val:
            return False
        left_check = same_tree(p.left, q.left)
        if left_check:
            right_check = same_tree(p.right, q.right)
            return right_check
        else:
            return False
    if (p and not q) or (q and not p):
        return False

    return True


if __name__ == "__main__":
    tree_node_1 = TreeNode(1)
    tree_node_1.left = TreeNode(2)
    tree_node_1.right = TreeNode(3)

    tree_node_2 = TreeNode(1)
    tree_node_2.left = TreeNode(2)
    tree_node_2.right = TreeNode(3)

    print(same_tree(tree_node_1, tree_node_2))
