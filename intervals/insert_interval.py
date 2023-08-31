from typing import List


def insert_interval(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    You are given an array of non-overlapping intervals where intervals[i] = [start_i, end_i] represent
    the start and the end of the ith interval and intervals is sorted in ascending order by start_i.

    You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

    Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and
    intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

    Return intervals after the insertion.

    Args:
        intervals: an array of non-overlapping intervals sorted in ascending order of start_i
        newInterval: an interval with start and end

    Returns:
        intervals after inserting newInterval in existing list of intervals
    """
    # Naive Solution
    output_interval = []
    inserted = False

    for interval in intervals:
        if inserted or newInterval[0] > interval[1]:
            output_interval.append(interval)
        else:
            if newInterval[1] < interval[0]:
                output_interval.append(newInterval)
                output_interval.append(interval)
                inserted = True

            if interval[0] <= newInterval[0] <= interval[1]:
                newInterval[0] = interval[0]

            if interval[0] <= newInterval[1] <= interval[1]:
                newInterval[1] = interval[1]

    if not inserted:
        output_interval.append(newInterval)

    return output_interval


if __name__ == "__main__":
    print(insert_interval([[1, 3], [6, 9]], [2, 5]))
    print(insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(insert_interval([], [5, 7]))
    print(insert_interval([[1, 5]], [2, 3]))
    print(insert_interval([[1, 5]], [2, 7]))
