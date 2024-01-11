from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_diff_between_node_and_ancestor(root: Optional[TreeNode]) -> int:
    """
    Given the root of a binary tree, find the maximum value v for which there exist
    different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

    A node a is an ancestor of b if either: any child of a is equal to b or
    any child of a is an ancestor of b.

    Args:
        root: root of a binary tree

    Returns:
        maximum difference between node and ancestor
    """
    # # Initial Solution keeping track of parents as an array
    # if not root:
    #     return 0
    #
    # max_diff = 0
    #
    # def traversal(node: Optional[TreeNode], parents: List[int]):
    #     nonlocal max_diff
    #     # print(f"parents: {parents}")
    #     if node:
    #         for par in parents:
    #             max_diff = max(max_diff, abs(node.val - par))
    #
    #         parents.append(node.val)
    #         if node.left:
    #             traversal(node.left, parents)
    #             parents.pop()
    #
    #         if node.right:
    #             traversal(node.right, parents)
    #             parents.pop()
    #
    # traversal(root, [])
    #
    # return max_diff

    # Refactored solution using keeping track of min and max value
    if not root:
        return 0

    max_diff = 0

    def traversal(node: Optional[TreeNode], min_val: int, max_val: int):
        nonlocal max_diff
        if node:
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            max_diff = max(max_diff, max_val - min_val)

            if node.left:
                traversal(node.left, min_val, max_val)

            if node.right:
                traversal(node.right, min_val, max_val)

    traversal(root, root.val, root.val)

    return max_diff


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(0)
    root.right.right.left = TreeNode(3)
    print(max_diff_between_node_and_ancestor(root))
