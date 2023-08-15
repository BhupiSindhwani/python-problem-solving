from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_list_with_random_pointer(head: 'Optional[Node]') -> 'Optional[Node]':
    """
    A linked list of length n is given such that each node contains an additional random pointer,
    which could point to any node in the list, or null.

    Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
    where each new node has its value set to the value of its corresponding original node.
    Both the next and random pointer of the new nodes should point to new nodes in the copied list such that
    the pointers in the original list and copied list represent the same list state.
    None of the pointers in the new list should point to nodes in the original list.

    For example, if there are two nodes X and Y in the original list, where X.random --> Y,
    then for the corresponding two nodes x and y in the copied list, x.random --> y.

    Return the head of the copied linked list.

    The linked list is represented in the input/output as a list of n nodes.
    Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to,
    or null if it does not point to any node.

    Your code will only be given the head of the original linked list.

    Args:
        head: head of the original linked list

    Returns:
        the head of the copied linked list
    """
    if not head:
        return

    node_map = {}
    dummy = Node(0)
    left = dummy
    right = None

    # populate new list with elements and create a hash map of original node to new node
    curr = head
    while curr:
        right = Node(curr.val)
        left.next = right
        node_map[curr] = right
        curr = curr.next
        left = right
    right.next = None

    curr = head
    new_curr = dummy.next
    while curr:
        if curr.random:
            new_curr.random = node_map[curr.random]
        else:
            new_curr.random = None
        curr = curr.next
        new_curr = new_curr.next

    return dummy.next


def print_linked_list(head: Optional[Node]) -> None:
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print()


if __name__ == "__main__":
    pass
