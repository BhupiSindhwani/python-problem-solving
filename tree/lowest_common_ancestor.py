class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
    as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

    Args:
        root: root of a binary tree
        p: a tree node
        q: a tree node

    Returns:
        node of the lowest common ancestor of the nodes containing value p and q
    """
    min_val, max_val = min(p.val, q.val), max(p.val, q.val)
    if (min_val < root.val < max_val or
            root.val == min_val or
            root.val == max_val):
        return root

    if root.val > max_val:
        return lowest_common_ancestor(root.left, p, q)

    elif root.val < min_val:
        return lowest_common_ancestor(root.right, p, q)


if __name__ == "__main__":
    tree_node = TreeNode(6)
    tree_node.left = TreeNode(2)
    tree_node.right = TreeNode(8)
    tree_node.left.left = TreeNode(0)
    tree_node.left.right = TreeNode(4)
    tree_node.left.right.left = TreeNode(3)
    tree_node.left.right.right = TreeNode(5)
    tree_node.right.left = TreeNode(7)
    tree_node.right.right = TreeNode(9)

    print(lowest_common_ancestor(tree_node, TreeNode(2), TreeNode(8)).val)
