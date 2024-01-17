from collections import defaultdict
from typing import List


def unique_number_of_occurrences(arr: List[int]) -> bool:
    """
    Given an array of integers arr, return true if the number of occurrences of each value
    in the array is unique or false otherwise.

    Args:
        arr: an input array of integers

    Returns:
        true if the number of occurrence of each value in the input array is unique
    """
    freq_set = set()

    num_freq = defaultdict(int)

    for num in arr:
        num_freq[num] += 1

    for val in num_freq.values():
        if val in freq_set:
            return False
        else:
            freq_set.add(val)

    return True


if __name__ == '__main__':
    print(unique_number_of_occurrences([1, 2, 2, 1, 1, 3]))
    print(unique_number_of_occurrences([1, 2]))
    print(unique_number_of_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
