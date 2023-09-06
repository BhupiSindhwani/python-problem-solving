from typing import List


def single_number(nums: List[int]) -> int:
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

    You must implement a solution with a linear runtime complexity and use only constant extra space.

    Args:
        nums: a non-empty array of integers

    Returns:
        the element that appears only once (there will be only one such element in the input array)
    """
    curr_num = nums[0]
    for num in nums[1:]:
        curr_num ^= num

    return curr_num


if __name__ == "__main__":
    print(single_number([2, 2, 1]))
    print(single_number([4, 1, 2, 1, 2]))
    print(single_number([1]))
