from typing import List


def max_product_subarray(nums: List[int]) -> int:
    """
    Given an integer array nums, find a subarray that has the largest product, and return the product.

    Args:
        nums: an integer array

    Returns:
        the product of a subarray that has the largest product
    """
    max_prod = float('-inf')
    curr_min, curr_max = 1, 1

    for num in nums:
        # print(f"curr_min: {curr_min}; curr_max: {curr_max}; max_prod: {max_prod}; num: {num}")
        val1 = curr_min * num
        val2 = curr_max * num
        curr_min = min(val1, val2, num)
        curr_max = max(val1, val2, num)
        max_prod = max(max_prod, curr_max)

    return max_prod


if __name__ == '__main__':
    print(max_product_subarray([2, 3, -2, 4]))
    print(max_product_subarray([2, -3, 3, -1, 4]))
    print(max_product_subarray([-2, 0, -1]))
    print(max_product_subarray([-2, 0, 4, 5, -1]))
    print(max_product_subarray([-2, 3, -4]))
