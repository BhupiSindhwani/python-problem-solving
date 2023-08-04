from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Given an integer array nums, return all the triplets
    [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Args:
        nums: an integer array

    Returns:
        array containing the list of all non-duplicate triplets that add up to 0
    """
    nums.sort()  # sort the array

    triplets = []

    for idx, num in enumerate(nums):

        if idx > 0 and num == nums[idx - 1]:
            continue

        left, right = idx + 1, len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum > -nums[idx]:
                right -= 1
            elif curr_sum < -nums[idx]:
                left += 1
            else:
                triplets.append([nums[idx], nums[left], nums[right]])
                left += 1
                right -= 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return triplets


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    print(three_sum([0, 1, 1]))
    print(three_sum([0, 0, 0]))
    print(three_sum([-2, 0, 0, 2, 2]))

    #   -4 -1 -1 0 1 2
    #   -2  0  0 2 2
