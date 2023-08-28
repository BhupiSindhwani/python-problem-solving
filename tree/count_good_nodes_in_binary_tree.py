from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_good_nodes_in_binary_tree(root: TreeNode) -> int:
    """
    Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes
    with a value greater than X.

    Return the number of good nodes in the binary tree.

    Args:
        root: root of binary tree

    Returns:
        the number of good nodes in the given binary tree
    """
    # # Solution using BFS
    # queue = deque()
    # num_good_nodes = 0
    #
    # if root:
    #     num_good_nodes += 1
    #     queue.append((root, root.val))
    #
    # while queue:
    #     queue_len = len(queue)
    #     for _ in range(queue_len):
    #         node, max_val = queue.popleft()
    #         if node.left:
    #             if node.left.val >= max_val:
    #                 num_good_nodes += 1
    #             queue.append((node.left, max(node.left.val, max_val)))
    #         if node.right:
    #             if node.right.val >= max_val:
    #                 num_good_nodes += 1
    #             queue.append((node.right, max(node.right.val, max_val)))
    #
    # return num_good_nodes

    # Solution using DFS
    num_good_nodes = 0

    def preorder_traversal(node: Optional[TreeNode], max_val: int) -> None:

        nonlocal num_good_nodes

        if node:
            if node.val >= max_val:
                num_good_nodes += 1
            max_val = max(max_val, node.val)
            preorder_traversal(node.left, max_val)
            preorder_traversal(node.right, max_val)

    preorder_traversal(root, root.val)

    return num_good_nodes


if __name__ == "__main__":
    tree_node = TreeNode(3)
    tree_node.left = TreeNode(1)
    tree_node.right = TreeNode(4)
    tree_node.left.left = TreeNode(3)
    tree_node.right.left = TreeNode(1)
    tree_node.right.right = TreeNode(5)

    print(count_good_nodes_in_binary_tree(tree_node))

    tree_node = TreeNode(9)
    tree_node.right = TreeNode(3)
    tree_node.right.left = TreeNode(6)

    print(count_good_nodes_in_binary_tree(tree_node))
