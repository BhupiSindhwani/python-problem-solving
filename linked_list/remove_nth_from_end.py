from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

    Args:
        head: head of a linked list
        n: integer depicting the nth node

    Returns:
        head of the linked list after remove the nth node from the end of the list
    """
    # Initial Solution
    # prev, curr = None, head
    #
    # count = 0
    # while curr:
    #     if count < n:
    #         curr = curr.next
    #         count += 1
    #     else:
    #         if not prev:
    #             prev = head
    #         else:
    #             prev = prev.next
    #         curr = curr.next
    #
    # if not prev:
    #     head = head.next
    # else:
    #     prev.next = prev.next.next
    #
    # return head

    # Revised (simplified) Solution using dummy note pattern
    dummy = ListNode(0, head)
    prev, curr = dummy, head

    count = 0
    while curr:
        if count < n:
            curr = curr.next
            count += 1
        else:
            prev = prev.next
            curr = curr.next

    prev.next = prev.next.next

    return dummy.next


if __name__ == "__main__":
    head_node = ListNode(1)
    head_node.next = ListNode(2)
    head_node.next.next = ListNode(3)
    head_node.next.next.next = ListNode(4)
    head_node.next.next.next.next = ListNode(5)

    head_node = remove_nth_from_end(head_node, 5)
    node = head_node
    while node:
        print(f"{node.val}->", end="")
        node = node.next
    print(None)
