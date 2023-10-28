from typing import List


def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    Given an integer array nums, return the length of the longest strictly increasing subsequence.

    Args:
        nums: an integer array

    Returns:
        the length of the longest strictly increasing subsequence
    """
    # # Solution using dp - O(n^2)
    # dp = [1] * len(nums)
    # max_len = 1
    #
    # for i in range(len(nums) - 2, -1, -1):
    #     # print(dp)
    #     for j in range(i + 1, len(dp)):
    #         if nums[i] < nums[j]:
    #             dp[i] = max(dp[i], 1 + dp[j])
    #     max_len = max(max_len, dp[i])
    # return max_len

    # Solution using binary search - O(nlog(n))
    def binary_search(numbers: List[int], val: int) -> int:
        left, right = 0, len(numbers)
        idx_of_interest = 0  # index of subsequence with value greater than val
        while left <= right:
            mid = left + ((right - left) // 2)
            if val > numbers[mid]:
                left = mid + 1
            elif val < numbers[mid]:
                right = mid - 1
                idx_of_interest = mid
            else:
                idx_of_interest = mid
                break
        return idx_of_interest

    max_subsequence= []

    for idx in range(len(nums)):
        if len(max_subsequence) == 0 or nums[idx] > max_subsequence[-1]:
            max_subsequence.append(nums[idx])
        else:
            pd = binary_search(max_subsequence, nums[idx])
            max_subsequence[pd] = nums[idx]

    # print(max_subsequence)
    return len(max_subsequence)


if __name__ == '__main__':
    print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
    print(longest_increasing_subsequence([0, 1, 0, 3, 2, 3]))
    print(longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]))
    print(longest_increasing_subsequence([1, 3, 6, 7, 9, 4, 10, 5, 6]))
