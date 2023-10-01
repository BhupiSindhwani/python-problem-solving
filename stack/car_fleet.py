from typing import List


def car_fleet(target: int, position: List[int], speed: List[int]) -> int:
    """
    There are n cars going to the same destination along a one-lane road. The destination is target miles away.

    You are given two integer array position and speed, both of length n, where
    position[i] is the position of the ith car and
    speed[i] is the speed of the ith car (in miles per hour).

    A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper
    at the same speed. The faster car will slow down to match the slower car's speed.
    The distance between these two cars is ignored (i.e., they are assumed to have the same position).

    A car fleet is some non-empty set of cars driving at the same position and same speed.
    Note that a single car is also a car fleet.

    If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

    Return the number of car fleets that will arrive at the destination.

    Args:
        target: an integer representing the target miles
        position: an integer array of positions
        speed: an integer array of speed

    Returns:
        the number of car fleets that will arrive at the destination
    """
    # # Solution using stack
    # pairs = [(p, s) for p,s in zip(position, speed)]
    # stack = []
    #
    # for p, s in sorted(pairs)[::-1]:
    #     time = (target - p) / s
    #     stack.append(time)
    #     if len(stack) >= 2 and time <= stack[-2]:
    #         stack.pop()
    #
    # return len(stack)

    # Solution using counter
    pos_speed = list(zip(position, speed))
    pos_speed.sort(key=lambda x: x[0], reverse=True)

    num_fleets = 1
    prev_time = (target - pos_speed[0][0]) / pos_speed[0][1]
    for pos, sp in pos_speed:
        curr_time = (target - pos) / sp
        if prev_time < curr_time:
            num_fleets += 1
            prev_time = curr_time

    return num_fleets


if __name__ == "__main__":
    print(car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print(car_fleet(10, [3], [3]))
    print(car_fleet(100, [0, 2, 4], [4, 2, 1]))
    print(car_fleet(10, [0, 4, 2], [2, 1, 3]))
