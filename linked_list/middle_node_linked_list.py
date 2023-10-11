from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.

    Args:
        head: head of a singly linked list

    Returns:
        the middle node of the linked list
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == '__main__':
    head_node_list = ListNode(1)
    head_node_list.next = ListNode(2)
    head_node_list.next.next = ListNode(3)
    head_node_list.next.next.next = ListNode(4)
    head_node_list.next.next.next.next = ListNode(5)
    head_node_list.next.next.next.next.next = ListNode(6)

    node = middle_node_linked_list(head_node_list)

    while node:
        print(f"{node.val}->", end="")
        node = node.next
    print(None)
