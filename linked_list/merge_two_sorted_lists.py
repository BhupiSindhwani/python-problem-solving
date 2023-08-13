from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_sorted_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists into one sorted list. The list should be made by splicing together the nodes
    of the first two lists.

    Return the head of the merged linked list.

    Args:
        list1: head of a sorted (in non-decreasing order) linked list
        list2: head of a sorted (in non-decreasing order) linked list

    Returns:
        the head of the merged linked list
    """
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next


if __name__ == "__main__":
    head_node_list1 = ListNode(1)
    head_node_list1.next = ListNode(2)
    head_node_list1.next.next = ListNode(4)

    head_node_list2 = ListNode(1)
    head_node_list2.next = ListNode(3)
    head_node_list2.next.next = ListNode(4)

    node = merge_two_sorted_lists(head_node_list1, head_node_list2)
    while node:
        print(f"{node.val}->", end="")
        node = node.next
    print(None)
