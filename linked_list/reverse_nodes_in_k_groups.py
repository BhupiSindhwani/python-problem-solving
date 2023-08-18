from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_nodes_in_k_groups(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

    k is a positive integer and is less than or equal to the length of the linked list.
    If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

    You may not alter the values in the list's nodes, only nodes themselves may be changed.

    Args:
        head: head of a linked list
        k: a positive integer and is less than or equal to the length of the linked list

    Returns:
        the head of the modified list
    """
    dummy = ListNode(0, head)
    group_prev = dummy

    def get_kth_node(curr_node, k):
        while curr_node and k > 0:
            curr_node = curr_node.next
            k -= 1
        return curr_node

    while True:
        kth_node = get_kth_node(group_prev, k)
        if not kth_node:
            break

        group_next = kth_node.next
        prev, curr = kth_node.next, group_prev.next
        while curr != group_next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        temp = group_prev.next
        group_prev.next = kth_node
        group_prev = temp

    return dummy.next


if __name__ == "__main__":
    head_node = ListNode(1)
    head_node.next = ListNode(2)
    head_node.next.next = ListNode(3)
    head_node.next.next.next = ListNode(4)
    head_node.next.next.next.next = ListNode(5)

    node = reverse_nodes_in_k_groups(head_node, 2)
    while node:
        print(f"{node.val}->", end="")
        node = node.next
    print(None)
