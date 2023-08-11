import math
from typing import List


def koko_eating_bananas(piles: List[int], h: int) -> int:
    """
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
    The guards have gone and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k.
    Each hour, she chooses some pile of bananas and eats k bananas from that pile.
    If the pile has less than k bananas, she eats all of them instead and
    will not eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

    Return the minimum integer k such that she can eat all the bananas within h hours.

    Args:
        piles: an integer array representing n piles of bananas
        h: integer representing hours

    Returns:
        minimum integer k such that koko can eat all the bananas within h hours
    """
    left, right = 1, max(piles)
    result = right

    while left <= right:
        mid = (left + right) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)
        if hours <= h:
            result = min(result, mid)
            right = mid - 1
        elif hours > h:
            left = mid + 1

    return result


if __name__ == "__main__":
    print(koko_eating_bananas([3, 6, 7, 11], 8))
    print(koko_eating_bananas([30, 11, 23, 4, 20], 5))
    print(koko_eating_bananas([30, 11, 23, 4, 20], 6))
    print(koko_eating_bananas([312884470], 312884469))
