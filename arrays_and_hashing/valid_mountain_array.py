from typing import List


def valid_mountain_array(arr: List[int]) -> bool:
    """
    Given an array of integers arr, return true if and only if it is a valid mountain array.

    Recall that arr is a mountain array if and only if:

    - arr.length >= 3
    - There exists some i with 0 < i < arr.length - 1 such that:
        - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

    Args:
        arr: an integer array

    Returns:
        true if and only if the input array is a valid mountain array
    """
    if len(arr) < 3:
        return False

    idx = 1

    # check for walking up to peak
    while idx < len(arr):
        if arr[idx] > arr[idx - 1]:
            idx += 1
        else:
            if idx == 1:  # check for only downhill
                return False
            break

    if idx == len(arr):  # check for only uphill
        return False

    # check for walking down from the peak
    while idx < len(arr):
        if arr[idx] < arr[idx - 1]:
            idx += 1
        else:
            break

    return True if idx >= len(arr) else False


if __name__ == '__main__':
    print(valid_mountain_array([2, 1]))
    print(valid_mountain_array([3, 5, 5]))
    print(valid_mountain_array([0, 3, 2, 1]))
