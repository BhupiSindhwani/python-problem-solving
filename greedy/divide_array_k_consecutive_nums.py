import heapq
from typing import List


def divide_array_k_consecutive_nums(nums: List[int], k: int) -> bool:
    """
    Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into
    sets of k consecutive numbers.

    Return true if it is possible. Otherwise, return false.

    Args:
        nums: an integer array
        k: a positive integer

    Returns:
        true if it is possible to divide input array into sets of k consecutive numbers, otherwise false
    """
    # Check if the nums size is divisible by k
    if len(nums) % k:
        return False

    # Create a nums map
    nums_count = {}
    for num in nums:
        nums_count[num] = nums_count.get(num, 0) + 1

    # Create a min heap of nums count keys
    nums_heap = list(nums_count.keys())
    heapq.heapify(nums_heap)

    # Look while heap is non-empty
    while nums_heap:
        top_num = nums_heap[0]
        for val in range(top_num, top_num + k):
            if val not in nums_count:
                return False
            nums_count[val] -= 1
            if nums_count[val] == 0:
                if val != nums_heap[0]:
                    return False
                heapq.heappop(nums_heap)

    return True


if __name__ == '__main__':
    print(divide_array_k_consecutive_nums([1, 2, 3, 3, 4, 4, 5, 6], 4))
    print(divide_array_k_consecutive_nums([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3))
    print(divide_array_k_consecutive_nums([1, 2, 3, 4], 3))
