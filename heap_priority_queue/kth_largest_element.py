"""
Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element
representing the kth largest element in the stream.
"""
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    kth_largest = KthLargest(3, [4, 5, 8, 2])
    print(kth_largest.add(3))
    print(kth_largest.add(5))
    print(kth_largest.add(10))
    print(kth_largest.add(9))
    print(kth_largest.add(4))
