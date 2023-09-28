from collections import deque
from typing import List


def sort_array_by_parity(nums: List[int]) -> List[int]:
    """
    Given an integer array nums, move all the even integers at the beginning of the array followed by all
    the odd integers.

    Return any array that satisfies this condition.

    Args:
        nums: an integer array

    Returns:
        an array with all the even integers at the beginning of the array
    """
    # # Solution using deque
    # queue = deque()
    #
    # for num in nums:
    #     if num % 2 == 0:
    #         queue.appendleft(num)
    #     else:
    #         queue.append(num)
    #
    # return list(queue)

    # # Solution using sort
    # nums.sort(key=lambda x: x % 2)
    # return nums

    # # Solution using two list
    # even = []
    # odd = []
    #
    # for num in nums:
    #     if num % 2 == 0:
    #         even.append(num)
    #     else:
    #         odd.append(num)
    #
    # return even + odd

    # Solution using two pointers approach
    left, right = 0, len(nums) - 1

    while left < right:
        while left < right and nums[left] % 2 == 0:
            left += 1
        while left < right and nums[right] % 2 != 0:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]

    return nums


if __name__ == "__main__":
    print(sort_array_by_parity([3, 1, 2, 4]))
    print(sort_array_by_parity([3, 1, 2, 4, 5, 9, 2]))
    print(sort_array_by_parity([8, 3, 1, 2, 4, 5, 9, 2]))
    print(sort_array_by_parity([0]))
    print(sort_array_by_parity([0, 1]))
