import heapq
from typing import List


def last_stone_weight(stones: List[int]) -> int:
    """
    You are given an array of integers stones where stones[i] is the weight of the ith stone.

    We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
    Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
    At the end of the game, there is at most one stone left.

    Return the weight of the last remaining stone. If there are no stones left, return 0.

    Args:
        stones: an array of integers stones where stones[i] is the weight of the ith stone

    Returns:
        the weight of the last remaining stone, otherwise 0
    """
    max_heap = []

    for stone in stones:
        heapq.heappush(max_heap, stone * -1)

    while len(max_heap) >= 2:
        y = heapq.heappop(max_heap) * -1
        x = heapq.heappop(max_heap) * -1
        if x != y:
            heapq.heappush(max_heap, (y - x) * -1)

    return max_heap[0] * -1 if max_heap else 0


if __name__ == "__main__":
    print(last_stone_weight([2, 7, 4, 1, 8, 1]))
    print(last_stone_weight([1]))
