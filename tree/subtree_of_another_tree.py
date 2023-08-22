from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def subtree_of_another_tree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """
    Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the
    same structure and node values of subRoot and false otherwise.

    A subtree of a binary tree is a tree that consists of a node in tree and all of this node's descendants.
    The tree could also be considered as a subtree of itself.

    Args:
        root: root of a binary tree
        subRoot: root of a binary tree

    Returns:
        true if subRoot is a subtree of root with the same structure and node values, otherwise false
    """
    if not subRoot:
        return True
    if not root:
        return False

    if same_tree(root, subRoot):
        return True

    return (subtree_of_another_tree(root.left, subRoot) or
            subtree_of_another_tree(root.right, subRoot))


def same_tree(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
    if tree1 and tree2:
        if tree1.val != tree2.val:
            return False
        left = same_tree(tree1.left, tree2.left)
        if left:
            right = same_tree(tree1.right, tree2.right)
            return right
        else:
            return False
    if (tree1 and not tree2) or (tree2 and not tree1):
        return False
    return True


if __name__ == "__main__":
    tree_node_1 = TreeNode(3)
    tree_node_1.left = TreeNode(4)
    tree_node_1.right = TreeNode(5)
    tree_node_1.left.left = TreeNode(1)
    tree_node_1.left.right = TreeNode(2)
    tree_node_1.left.right.left = TreeNode(0)
    tree_node_1.left.right.right = TreeNode(4)
    tree_node_1.left.right.right.left = TreeNode(1)
    tree_node_1.left.right.right.right = TreeNode(2)

    tree_node_2 = TreeNode(4)
    tree_node_2.left = TreeNode(1)
    tree_node_2.right = TreeNode(2)

    print(subtree_of_another_tree(tree_node_1, tree_node_2))
