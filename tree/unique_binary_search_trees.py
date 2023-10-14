from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def unique_binary_search_trees(n: int) -> List[Optional[TreeNode]]:
    """
    Given an integer n, return all the structurally unique BST's (binary search trees),
    which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

    Args:
        n: an integer

    Returns:
        all the structurally unique BST's which has exactly n nodes of unique values from 1 to n
    """
    dp = {}

    def generate(left: int, right: int) -> List[Optional[TreeNode]]:
        if left > right:
            return [None]

        if (left, right) in dp:
            return dp[(left, right)]

        result = []
        for val in range(left, right + 1):
            for left_tree in generate(left, val - 1):
                for right_tree in generate(val + 1, right):
                    root = TreeNode(val, left_tree, right_tree)
                    result.append(root)
        dp[(left, right)] = result
        return result

    return generate(1, n)


def pre_order_traversal(root: Optional[TreeNode]) -> None:
    if root:
        print(root.val, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


if __name__ == "__main__":
    trees = unique_binary_search_trees(4)
    if trees:
        for tree in trees:
            pre_order_traversal(tree)
            print()
