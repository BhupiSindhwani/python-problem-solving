from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and
    return an array of the non-overlapping intervals that cover all the intervals in the input.

    Args:
        intervals: an array of intervals

    Returns:
        an array of the non-overlapping intervals that cover all the intervals in the input
    """
    # # Initial Solution
    # if len(intervals) <= 1:
    #     return intervals
    #
    # output = []
    # intervals.sort(key=lambda x: x[0])
    # prev = intervals[0]
    #
    # for curr in intervals:
    #     if curr[0] <= prev[1]:
    #         prev[1] = max(prev[1], curr[1])
    #     else:
    #         output.append(prev)
    #         prev = curr
    #
    # output.append(prev)
    # return output

    # Refactored Solution
    intervals.sort(key=lambda x: x[0])  # Sort the intervals by starting interval
    merged_intervals = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged_intervals[-1][1]:
            merged_intervals[-1][1] = max(end, merged_intervals[-1][1])
        else:
            merged_intervals.append([start, end])

    return merged_intervals


if __name__ == "__main__":
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(merge_intervals([[1, 4], [4, 5]]))
    print(merge_intervals([[1, 4], [0, 4]]))
