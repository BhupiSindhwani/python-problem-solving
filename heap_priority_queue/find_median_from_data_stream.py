"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far.
"""
import heapq


class MedianFinder:

    def __init__(self):
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, num * -1)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, heapq.heappop(self.max_heap) * -1)

        if self.min_heap and self.max_heap[0] * -1 > self.min_heap[0]:
            max_heap_max = heapq.heappop(self.max_heap) * -1
            min_heap_min = heapq.heappop(self.min_heap) * -1
            heapq.heappush(self.min_heap, max_heap_max)
            heapq.heappush(self.max_heap, min_heap_min)

        self.count += 1

    def findMedian(self) -> float:
        even_total_count = self.count % 2 == 0
        if even_total_count:
            return ((self.max_heap[0] * -1) + self.min_heap[0]) / 2
        else:
            if len(self.max_heap) > len(self.min_heap):
                return self.max_heap[0] * -1
            else:
                return self.min_heap[0]


if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)            # arr = [1]
    medianFinder.addNum(2)            # arr = [1, 2]
    print(medianFinder.findMedian())   # return 1.5(i.e., (1 + 2) / 2)
    medianFinder.addNum(3)            # arr[1, 2, 3]
    print(medianFinder.findMedian())   # return 2.0

    medianFinder = MedianFinder()
    medianFinder.addNum(0)
    medianFinder.addNum(0)
    print(medianFinder.findMedian())
