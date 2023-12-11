import collections
from typing import List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    You are given an array of integers nums, there is a sliding window of size k which is moving
    from the very left of the array to the very right.

    You can only see the k numbers in the window. Each time the sliding window moves right by one position.

    Return the max sliding window.

    Args:
        nums: an array of integers
        k: window size (integer)

    Returns:
        an array of integers consisting of the maximum of each sliding window
    """
    # result = []
    #
    # if len(nums) < k:
    #     return result
    #
    # dq = collections.deque()
    #
    # start = end = 0
    #
    # while end < len(nums):
    #     while dq and nums[dq[-1]] < nums[end]:
    #         dq.pop()
    #     dq.append(end)
    #
    #     if start > dq[0]:
    #         dq.popleft()
    #
    #     if end + 1 >= k:
    #         result.append(nums[dq[0]])
    #         start += 1
    #
    #     end += 1
    #
    # return result

    # Refactored solution ( bit more intuitive)
    result = []
    queue = collections.deque()

    start, end = 0, 0

    while end < len(nums):
        # pop smaller values from the queue
        while queue and queue[-1] < nums[end]:
            queue.pop()
        queue.append(nums[end])

        if end + 1 >= k:
            result.append(queue[0])
            if nums[start] == queue[0]:
                queue.popleft()
            start += 1

        end += 1

    return result


if __name__ == "__main__":
    print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(max_sliding_window([1, 3, -1, 7, -4, 3, 5, 4, -3, 5, 3, 6, 7], 4))
    print(max_sliding_window([3, 3, 3, 3, -4, 3, 5, 4, -3, 5, 3, 6, 7], 4))
    print(max_sliding_window([1], 1))
    print(max_sliding_window([1, 3, 1, 2, 0, 5], 3))
