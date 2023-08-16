import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.

    Args:
        lists: an array of k linked-lists, each linked-list is sorted in ascending order

    Returns:
        merged sorted linked-list
    """
    # # Solution using Min Heap
    # min_heap = [(elem.val, idx, elem) for idx, elem in enumerate(lists) if lists[idx]]
    # dummy = ListNode(0)
    # tail = dummy
    #
    # heapq.heapify(min_heap)
    #
    # while min_heap:
    #     val, idx, elem = heapq.heappop(min_heap)
    #     tail.next = elem
    #     tail = tail.next
    #     lists[idx] = lists[idx].next
    #     if lists[idx]:
    #         heapq.heappush(min_heap, (lists[idx].val, idx, lists[idx]))
    #
    # return dummy.next

    # Solution using sorting the lists in pairs
    if not lists:
        return

    def merge_two_sorted_lists(l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next

    while len(lists) > 1:
        merged_list = []

        for idx in range(0, len(lists), 2):
            list1 = lists[idx]
            list2 = lists[idx + 1] if (idx + 1) < len(lists) else None

            merged_list.append(merge_two_sorted_lists(list1, list2))
        lists = merged_list

    return lists[0]


if __name__ == "__main__":
    head_node_list1 = ListNode(1)
    head_node_list1.next = ListNode(4)
    head_node_list1.next.next = ListNode(5)

    head_node_list2 = ListNode(1)
    head_node_list2.next = ListNode(3)
    head_node_list2.next.next = ListNode(4)

    head_node_list3 = ListNode(2)
    head_node_list3.next = ListNode(6)

    node = merge_k_sorted_lists([head_node_list1, head_node_list2, head_node_list3])
    # node = merge_k_sorted_lists([None])
    # node = merge_k_sorted_lists([])
    while node:
        print(f"{node.val}->", end="")
        node = node.next
    print(None)
