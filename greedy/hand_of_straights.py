import heapq
from typing import List


def hand_of_straights(hand: List[int], groupSize: int) -> bool:
    """
    Alice has some number of cards, and she wants to rearrange the cards into groups so that each group
    is of size groupSize, and consists of groupSize consecutive cards.

    Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize,
    return true if she can rearrange the cards, or false otherwise.

    Args:
        hand: an integer array where hand[i] is the value written on the ith card
        groupSize: integer

    Returns:
        true if cards can be rearranged as required, otherwise false
    """
    if len(hand) % groupSize:
        return False

    card_count = {}

    for card in hand:
        card_count[card] = card_count.get(card, 0) + 1

    card_heap = list(card_count.keys())
    heapq.heapify(card_heap)

    while card_heap:
        curr_card = card_heap[0]

        for val in range(curr_card, curr_card + groupSize):
            if val not in card_count:
                return False
            card_count[val] -= 1
            if card_count[val] == 0:
                if val != card_heap[0]:
                    return False
                heapq.heappop(card_heap)

    return True


if __name__ == "__main__":
    print(hand_of_straights([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
    print(hand_of_straights([1, 2, 3, 4, 5], 4))
    print(hand_of_straights([1], 1))
