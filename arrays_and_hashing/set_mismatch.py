from typing import List


def set_mismatch(nums: List[int]) -> List[int]:
    """
    You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

    You are given an integer array nums representing the data status of this set after the error.

    Find the number that occurs twice and the number that is missing and return them in the form of an array.

    Args:
        nums: input array

    Returns:
        an integer array containing the duplication num and missing num from the input array
    """
    nums_freq = {n: 1 for n in range(1, len(nums) + 1)}

    for num in nums:
        nums_freq[num] -= 1

    repeat, missing = 0, 0

    for num, freq in nums_freq.items():
        if freq == -1:
            repeat = num
        if freq == 1:
            missing = num

    return [repeat, missing]


if __name__ == '__main__':
    print(set_mismatch([1, 2, 2, 4]))
    print(set_mismatch([1, 1]))
    print(set_mismatch([2, 2]))
