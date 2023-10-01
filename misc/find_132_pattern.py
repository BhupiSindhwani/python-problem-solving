from typing import List


def find_132_pattern(nums: List[int]) -> bool:
    """
    Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k]
    such that i < j < k and nums[i] < nums[k] < nums[j].

    Return true if there is a 132 pattern in nums, otherwise, return false.

    Args:
        nums: an integer array

    Returns:
        true if there is a 132 pattern in nums, otherwise false
    """
    stack = []  # mono decreasing order or pair - (max val, min left val)
    min_val = nums[0]

    for num in nums[1:]:
        while stack and num >= stack[-1][0]:
            stack.pop()
        if stack and stack[-1][1] < num < stack[-1][0]:
            return True
        stack.append((num, min_val))
        min_val = min(min_val, num)

    return False


if __name__ == "__main__":
    print(find_132_pattern([1, 2, 3, 4]))
    print(find_132_pattern([3, 1, 4, 2]))
    print(find_132_pattern([-1, 3, 2, 0]))
    print(find_132_pattern([1, 0, 1, -4, -3]))
    print(find_132_pattern([3, 5, 0, 3, 4]))
