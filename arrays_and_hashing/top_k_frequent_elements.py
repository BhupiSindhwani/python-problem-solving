from typing import List


def top_k_frequent_elements(nums: List[int], k: int) -> List[int]:
    """
    Given an integer array nums and an integer k, return the k most frequent elements.

    Args:
        nums: an integer array
        k: integer

    Returns:
        k mos frequent elements
    """
    # Initial Solution
    # num_count = {}
    # for num in nums:
    #     num_count[num] = num_count.get(num, 0) + 1
    #
    # sorted_num_count = sorted(num_count.items(), key=lambda x: x[1], reverse=True)
    #
    # return [pair[0] for pair in sorted_num_count[:k]]

    # Improved Solution - O(n)
    num_count = {}
    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    num_freq = [[] for i in range(len(nums))]

    for num, count in num_count.items():
        num_freq[count-1].append(num)

    result = []
    for idx in range(len(num_freq) - 1, -1, -1):
        for num in num_freq[idx]:
            result.append(num)
            if len(result) == k:
                return result


if __name__ == "__main__":
    print(top_k_frequent_elements([1, 1, 1, 2, 2, 3], 2))
    print(top_k_frequent_elements([1], 1))
