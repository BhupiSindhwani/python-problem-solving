from typing import List


def non_overlapping_intervals(intervals: List[List[int]]) -> int:
    """
    Given an array of intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals
    you need to remove to make the rest of the intervals non-overlapping.

    Args:
        intervals: an array of intervals

    Returns:
        the minimum number of intervals to remove to make rest of the intervals non-overlapping
    """
    intervals.sort(key=lambda x: (x[0], x[1]))

    # print(intervals)

    prev = intervals[0]
    count = 0

    for interval in intervals[1:]:
        if interval[0] < prev[1]:
            count += 1
            prev[1] = min(prev[1], interval[1])
        else:
            prev = interval
    return count


if __name__ == "__main__":
    print(non_overlapping_intervals([[1, 2], [2, 3], [3, 4], [1, 3], [1, 4]]))
    print(non_overlapping_intervals([[1, 2], [1, 2], [1, 2]]))
    print(non_overlapping_intervals([[1, 2], [2, 3]]))
    print(non_overlapping_intervals([[1, 12], [12, 23], [-1, 0], [0, 10], [5, 10]]))
    print(non_overlapping_intervals([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]))
    print(non_overlapping_intervals(
        [[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98], [-63, 2],
         [30, 47], [-40, -26]]))
