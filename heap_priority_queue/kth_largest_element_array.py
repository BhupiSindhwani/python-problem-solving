import heapq
from typing import List


def kth_largest_element_array(nums: List[int], k: int) -> int:
    """
    Given an integer array nums and an integer k, return the kth largest element in the array.

    Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Can you solve it without sorting?

    Args:
        nums: an integer array
        k: an integer

    Returns:
        kth largest element in the nums array
    """
    # Solution using Heap
    # min_heap = []
    # for num in nums:
    #     heapq.heappush(min_heap, num)
    #     if len(min_heap) > k:
    #         heapq.heappop(min_heap)
    #
    # return min_heap[0]

    # Solution using Quick Select: Average Case O(n), Worst Case O(n^2)
    k = len(nums) - k

    def quick_select(left, right):
        pivot = nums[right]
        ptr = left

        for idx in range(left, right):
            if nums[idx] <= pivot:
                nums[ptr], nums[idx] = nums[idx], nums[ptr]
                ptr += 1
        nums[ptr], nums[right] = nums[right], nums[ptr]

        if k < ptr:
            return quick_select(left, ptr - 1)
        elif k > ptr:
            return quick_select(ptr + 1, right)
        else:
            return nums[ptr]

    return quick_select(0, len(nums) - 1)


if __name__ == "__main__":
    print(kth_largest_element_array([3, 2, 6, 5, 1, 4], 2))
    print(kth_largest_element_array([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
