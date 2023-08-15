from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Args:
        l1: head of a linked list representing a non-negative integer
        l2: head of a linked list representing a non-negative integer

    Returns:
        head of a linked list that represents the sum of two input integers
    """
    curr_l1, curr_l2 = l1, l2
    dummy = ListNode(0)
    output = dummy
    tens_carry = 0

    while curr_l1 or curr_l2:
        d1 = curr_l1.val if curr_l1 else 0
        d2 = curr_l2.val if curr_l2 else 0
        addition = d1 + d2 + tens_carry
        ones = addition % 10
        tens_carry = addition // 10
        dummy.next = ListNode(ones)
        dummy = dummy.next
        curr_l1 = curr_l1.next if curr_l1 else None
        curr_l2 = curr_l2.next if curr_l2 else None
    if tens_carry:
        dummy.next = ListNode(tens_carry)

    return output.next


if __name__ == "__main__":
    head_node_list1 = ListNode(9)
    head_node_list1.next = ListNode(9)
    head_node_list1.next.next = ListNode(9)

    head_node_list2 = ListNode(9)
    head_node_list2.next = ListNode(9)
    head_node_list2.next.next = ListNode(9)

    node = add_two_numbers(head_node_list1, head_node_list2)
    while node:
        print(f"{node.val}->", end="")
        node = node.next
    print(None)
