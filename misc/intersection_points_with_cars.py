from typing import List


def intersection_points_with_cars(nums: List[List[int]]) -> int:
    """
    You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line.
    For any index i, nums[i] = [start_i, end_i] where start_i is the starting point of the ith car and
    end_i is the ending point of the ith car.

    Return the number of integer points on the line that are covered with any part of a car.

    Args:
        nums: 2D integer array representing the coordinates of the cars parking on a number line

    Returns:
        the number of integer points on the line that are covered with any part of a car
    """
    nums.sort(key=lambda x: x[0])
    covered_distance, last_num = 0, 0
    for num_start, num_end in nums:
        if num_start > last_num:
            covered_distance += num_end - num_start + 1
        elif num_end < last_num:
            continue
        else:
            covered_distance += num_end - last_num
        last_num = num_end

    return covered_distance


if __name__ == '__main__':
    print(intersection_points_with_cars([[3, 6], [1, 5], [4, 7]]))
    print(intersection_points_with_cars([[1, 3], [5, 8]]))
