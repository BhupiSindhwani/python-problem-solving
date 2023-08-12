from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Args:
        head: head of a singly linked list

    Returns:
        reversed list
    """
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


if __name__ == "__main__":
    head_node = ListNode(1)
    head_node.next = ListNode(2)
    head_node.next.next = ListNode(3)
    head_node.next.next.next = ListNode(4)
    head_node.next.next.next.next = ListNode(5)

    node = reverse_linked_list(head_node)
    while node:
        print(f"{node.val}->", end="")
        node = node.next
    print(None)
