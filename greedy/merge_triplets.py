from typing import List


def merge_triplets(triplets: List[List[int]], target: List[int]) -> bool:
    """
    A triplet is an array of three integers. You are given a 2D integer array triplets,
    where triplets[i] = [ai, bi, ci] describes the ith triplet.

    You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

    To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

    - Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to
    become [max(ai, aj), max(bi, bj), max(ci, cj)].
    For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5],
    triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].

    Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.

    Args:
        triplets: a 2D integer array
        target: an integer array that describes the triplet to obtain

    Returns:
        true if it is possible to obtain target triplet as an element of triplets, otherwise false
    """
    check_indexes = {0, 1, 2}

    for triplet in triplets:
        curr_matched_indexes = set()
        for idx in range(len(triplet)):
            if triplet[idx] == target[idx]:
                curr_matched_indexes.add(idx)
            elif triplet[idx] > target[idx]:
                curr_matched_indexes = set()
                break
        for _ in curr_matched_indexes:
            if _ in check_indexes:
                check_indexes.remove(_)
        if not check_indexes:
            return True

    return False


if __name__ == "__main__":
    print(merge_triplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]))
    print(merge_triplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]))
    print(merge_triplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]))
    print(merge_triplets([[3, 1, 7], [1, 5, 10]], [3, 5, 7]))
