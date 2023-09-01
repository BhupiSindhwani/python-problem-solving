from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest_elem_bst(root: Optional[TreeNode], k: int) -> int:
    """
    Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the
    values of the nodes in the tree.

    Args:
        root: root of a binary search tree
        k: integer

    Returns:
        the kth smallest value (1-indexed) of all the values of the nodes in the tree
    """
    count = 0
    result = None

    def bst(node: Optional[TreeNode]) -> None:
        nonlocal count
        nonlocal result
        if not result:
            if node:
                bst(node.left)
                count += 1
                if count == k:
                    result = node.val
                bst(node.right)

    bst(root)
    return result


if __name__ == "__main__":
    tree_node = TreeNode(3)
    tree_node.left = TreeNode(1)
    tree_node.right = TreeNode(4)
    tree_node.left.right = TreeNode(2)

    print(kth_smallest_elem_bst(tree_node, 1))

    tree_node = TreeNode(5)
    tree_node.left = TreeNode(3)
    tree_node.right = TreeNode(6)
    tree_node.left.left = TreeNode(2)
    tree_node.left.right = TreeNode(4)
    tree_node.left.left.left = TreeNode(1)

    print(kth_smallest_elem_bst(tree_node, 3))
