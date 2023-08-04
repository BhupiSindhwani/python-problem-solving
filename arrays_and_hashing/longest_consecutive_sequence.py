from typing import List


def longest_consecutive_sequence(nums: List[int]) -> int:
    """
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    Args:
        nums: an unsorted array of integers

    Returns:
        the length of the longest consecutive elements sequence
    """
    nums_set = set(nums)

    max_seq_len = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            curr_seq_len = 1
            while num + 1 in nums_set:
                curr_seq_len += 1
                num += 1
            max_seq_len = max(max_seq_len, curr_seq_len)

    return max_seq_len


if __name__ == "__main__":
    print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
    print(longest_consecutive_sequence([100, 201, 203, 202, 207, 205, 206, 204, 4, 200, 1, 3, 2]))
    print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(longest_consecutive_sequence([1, 2, 0, 1]))
    print(longest_consecutive_sequence([]))
