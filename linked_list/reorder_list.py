from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    """
    You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.

    Args:
        head: head of a singly linked-list

    Returns:
         None
    """
    # find the mid-point to split the input list into two halves
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the right half
    curr = slow.next  # start of right half
    prev = slow.next = None  # set the end of the reordered list to None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    # traverse the two halves to reorder
    left = head
    right = prev

    while right:
        temp_left = left.next
        temp_right = right.next
        left.next = right
        right.next = temp_left
        left = temp_left
        right = temp_right


if __name__ == "__main__":
    head_node = ListNode(1)
    head_node.next = ListNode(2)
    head_node.next.next = ListNode(3)
    head_node.next.next.next = ListNode(4)
    head_node.next.next.next.next = ListNode(5)

    reorder_list(head_node)
    node = head_node
    while node:
        print(f"{node.val}->", end="")
        node = node.next
    print(None)
