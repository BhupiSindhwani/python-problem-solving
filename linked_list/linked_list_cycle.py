from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def linked_list_cycle(head: Optional[ListNode]) -> bool:
    """
    Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by
    continuously following the next pointer.

    Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
    Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.

    Args:
        head: head of a linked list

    Returns:
        true if there is a cycle in the given linked list, otherwise false
    """
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


if __name__ == "__main__":
    head_node_list = ListNode(3)
    node = ListNode(2)
    head_node_list.next = node
    head_node_list.next.next = ListNode(0)
    head_node_list.next.next.next = ListNode(-4)
    head_node_list.next.next.next = node

    print(linked_list_cycle(None))
    print(linked_list_cycle(head_node_list))
