from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to
    the product of all the elements of nums except nums[i].

    Args:
        nums: an integer array

    Returns:
        an answer array such that answer[i] is equal to the product of all elements except nums[i]
    """
    # Solution using division operator
    # zero_count = 0
    # nums_product_without_zero = 1
    # answer = []
    #
    # for num in nums:
    #     if num == 0:
    #         zero_count += 1
    #     else:
    #         nums_product_without_zero *= num
    #
    # for num in nums:
    #     if num != 0:
    #         if not zero_count:
    #             answer.append(nums_product_without_zero // num)
    #         else:
    #             answer.append(0)
    #     else:
    #         if zero_count > 1:
    #             answer.append(0)
    #         else:
    #             answer.append(nums_product_without_zero)
    #
    # return answer

    # Solution without using division operator
    prefix_product = 1
    postfix_product = 1
    answer = [1] * len(nums)

    for idx, num in enumerate(nums):
        answer[idx] = prefix_product
        prefix_product *= nums[idx]

    for idx in range(len(nums) - 1, -1, -1):
        answer[idx] *= postfix_product
        postfix_product *= nums[idx]

    return answer


if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))
    print(product_except_self([-1, 1, 0, -3, 3]))
    print(product_except_self([-1, 1, 0, -3, 0]))
