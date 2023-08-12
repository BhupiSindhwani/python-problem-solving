from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).

    Args:
        nums1: sorted array of size m
        nums2: sorted array of size n

    Returns:
        median of the two sorted arrays (merged)
    """
    total_nums_count = len(nums1) + len(nums2)
    target_nums_count = total_nums_count // 2
    l_array, r_array = nums1, nums2

    if len(nums1) > len(nums2):
        l_array, r_array = nums2, nums1

    left, right = 0, len(l_array) - 1

    while True:
        midl = (left + right) // 2
        idx_r = target_nums_count - midl - 2

        l_array_left = l_array[midl] if midl >= 0 else float('-inf')
        l_array_right = l_array[midl + 1] if midl + 1 < len(l_array) else float('inf')
        r_array_left = r_array[idx_r] if idx_r >= 0 else float('-inf')
        r_array_right = r_array[idx_r + 1] if idx_r + 1 < len(r_array) else float('inf')

        if l_array_left <= r_array_right and r_array_left <= l_array_right:
            if total_nums_count % 2 == 0:
                return (max(l_array_left, r_array_left) + min(l_array_right, r_array_right)) / 2
            else:
                return min(l_array_right, r_array_right)
        elif l_array_left > r_array_right:
            right = midl - 1
        else:
            left = midl + 1


if __name__ == "__main__":
    print(find_median_sorted_arrays([1, 3], [2]))
    print(find_median_sorted_arrays([1, 2], [3, 4]))
    print(find_median_sorted_arrays([1, 2, 3, 4, 7, 10], [3, 5, 7, 8]))
    print(find_median_sorted_arrays([1, 2, 3, 4, 7, 10], [2, 14, 15]))
    print(find_median_sorted_arrays([1, 2, 3, 4, 7, 10], [2, 14, 15, 18, 19, 20]))
    print(find_median_sorted_arrays([], [1]))
