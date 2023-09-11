"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or
another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized
to a string and this string can be deserialized to the original tree structure.
"""
from collections import deque
from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Encodes a tree to a single string.

        Args:
            root: root of a tree

        Returns:
            string representing serialized version of given tree
        """
        queue = deque()
        queue.append(root)
        output = []

        while queue:
            curr = queue.popleft()
            if curr:
                queue.append(curr.left)
                queue.append(curr.right)
                output.append(str(curr.val))
            else:
                output.append('null')

        return ",".join(output)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Decodes your encoded data to tree.

        Args:
            data: string representing serialized version of given tree

        Returns:
            root of given tree
        """
        data = data.split(",")
        if not data[0]:
            return TreeNode(None)

        data_queue = deque(data)
        queue = deque()
        root_data = data_queue.popleft()
        root = TreeNode(int(root_data)) if root_data != "null" else None
        queue.append(root)

        while data_queue:
            left_data = data_queue.popleft()
            right_data = data_queue.popleft()
            curr_node = queue.popleft()
            if left_data != "null":
                curr_node.left = TreeNode(int(left_data))
                queue.append(curr_node.left)
            if right_data != "null":
                curr_node.right = TreeNode(int(right_data))
                queue.append(curr_node.right)

        return root


if __name__ == "__main__":
    tree_node = TreeNode(1)
    tree_node.left = TreeNode(2)
    tree_node.right = TreeNode(3)
    tree_node.right.left = TreeNode(4)
    tree_node.right.right = TreeNode(5)

    ser = Codec()
    deser = Codec()
    print(ser.serialize(tree_node))
    print(ser.serialize(deser.deserialize(ser.serialize(tree_node))))

    ser = Codec()
    deser = Codec()
    print(ser.serialize(None))
    print(ser.serialize(deser.deserialize(ser.serialize(None))))
