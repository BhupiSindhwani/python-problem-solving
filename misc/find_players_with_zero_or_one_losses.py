from typing import List


def find_players_with_zero_or_one_losses(matches: List[List[int]]) -> List[List[int]]:
    """
    You are given an integer array matches where matches[i] = [winner_i, loser_i]
    indicates that the player winner_i defeated player loser_i in a match.

    Return a list answer of size 2 where:

    - answer[0] is a list of all players that have not lost any matches.
    - answer[1] is a list of all players that have lost exactly one match.
    - The values in the two lists should be returned in increasing order.

    Note:

    You should only consider the players that have played at least one match.

    Args:
        matches: an integer array where matches[i] = [winner_i, loser_i]

    Returns:
        list answer where answer[0]: zero losses and answer[1]: one loss
    """
    only_loosers, only_winners, onetime_loosers = set(), set(), set()

    for winner, looser in matches:
        if winner in only_loosers:
            if winner in only_winners:
                only_winners.remove(winner)
        else:
            only_winners.add(winner)

        if looser in only_loosers:
            if looser in only_winners:
                only_winners.remove(winner)
            if looser in onetime_loosers:
                onetime_loosers.remove(looser)
        else:
            if looser in only_winners:
                only_winners.remove(looser)
            only_loosers.add(looser)
            onetime_loosers.add(looser)

    return [sorted(list(only_winners)), sorted(list(onetime_loosers))]


if __name__ == '__main__':
    print(find_players_with_zero_or_one_losses(
        [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
    ))
    print(find_players_with_zero_or_one_losses([[2, 3], [1, 3], [5, 4], [6, 4]]
                                               ))
