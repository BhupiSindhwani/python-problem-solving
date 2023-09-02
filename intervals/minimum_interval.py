import heapq
from typing import List


def minimum_interval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    """
    You are given a 2D integer array intervals, where intervals[i] = [left_i, right_i] describes the ith interval
    starting at left_i and ending at right_i (inclusive). The size of an interval is defined as the number of integers
    it contains, or more formally right_i - left_i + 1.

    You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i
    such that left_i <= queries[j] <= right_i. If no such interval exists, the answer is -1.

    Return an array containing the answers to the queries.

    Args:
        intervals: a 2D integer array representing intervals
        queries: an integer array representing queries

    Returns:
        an array containing the answers to the queries
    """
    intervals.sort()
    min_heap = []
    query_map = {}
    idx = 0

    for query in sorted(queries):
        while idx < len(intervals) and query >= intervals[idx][0]:
            heapq.heappush(min_heap, (intervals[idx][1] - intervals[idx][0] + 1, intervals[idx][1]))
            idx += 1

        while min_heap and query > min_heap[0][1]:
            heapq.heappop(min_heap)

        query_map[query] = min_heap[0][0] if min_heap else -1

    return [query_map[query] for query in queries]


if __name__ == "__main__":
    print(minimum_interval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]))
    print(minimum_interval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]))
