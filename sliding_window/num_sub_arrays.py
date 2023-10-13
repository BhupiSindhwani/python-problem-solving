from typing import List


def num_sub_arrays(arr: List[int], k: int, threshold: int) -> int:
    """
    Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and
    average greater than or equal to threshold.

    Args:
        arr: an integer array
        k: an integer
        threshold: an integer

    Returns:
        the number of sub-arrays of size k and average greater than or equal to threshold
    """
    count, curr_sum, target_sum = 0, 0, k * threshold
    start, end = 0, 0
    # result = []

    while end < len(arr):
        curr_sum += arr[end]
        if end - start + 1 == k:
            if curr_sum >= target_sum:
                count += 1
                # result.append(arr[start: end+1])
            curr_sum -= arr[start]
            start += 1
        end += 1

    # print(result)
    return count


if __name__ == '__main__':
    print(num_sub_arrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
    print(num_sub_arrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))
