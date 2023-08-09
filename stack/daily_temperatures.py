from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    Given an array of integers temperatures represents the daily temperatures,
    return an array answer such that answer[i] is the number of days you have to wait
    after the ith day to get a warmer temperature.

    If there is no future day for which this is possible, keep answer[i] == 0 instead.

    Args:
        temperatures: an array of integers representing daily temperatures

    Returns:
        an array such that answer[i] is the # of days you have to wait after the ith day to get a warmer temperature.
    """
    stack = []
    answer = [0] * len(temperatures)

    for idx, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            answer[stack[-1][1]] = idx - stack[-1][1]
            stack.pop()
        stack.append((temp, idx))

    return answer


if __name__ == "__main__":
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(daily_temperatures([30, 40, 50, 60]))
    print(daily_temperatures([30, 60, 90]))
    print(daily_temperatures([30]))
