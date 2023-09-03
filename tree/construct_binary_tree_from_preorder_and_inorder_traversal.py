from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
    inorder is the inorder traversal of the same tree, construct and return the binary tree.

    Args:
        preorder: an integer array representing preorder traversal of a binary tree
        inorder: an integer array representing inorder traversal of a binary tree

    Returns:
        the root node of the binary tree
    """
    if len(preorder) > 0:
        curr_root = TreeNode(preorder[0])
        left_elem_count = inorder.index(preorder[0])
        curr_root.left = build_tree(preorder[1:left_elem_count+1], inorder[:left_elem_count])
        curr_root.right = build_tree(preorder[left_elem_count+1:], inorder[left_elem_count+1:])

        return curr_root


if __name__ == "__main__":
    print(build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
    print(build_tree([-1], [-1]))
