import heapq
import math
from typing import List


def k_closest_points_to_origin(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
    return the k closest points to the origin (0, 0).

    The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

    You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

    Args:
        points: an array of points where points[i] = [xi, yi] represents a pint on the X-Y plane
        k: an integer k

    Returns:
        k closest points to the origin (0, 0)
    """
    max_heap = []
    closest_points = []

    for idx, point in enumerate(points):
        x, y = point
        heapq.heappush(max_heap, (math.sqrt((x**2) + (y**2)) * -1, idx))
        while len(max_heap) > k:
            heapq.heappop(max_heap)

    for elem in max_heap:
        closest_points.append(points[elem[1]])

    return closest_points


if __name__ == "__main__":
    print(k_closest_points_to_origin([[1, 3], [-2, 2]], 1))
    print(k_closest_points_to_origin([[3, 3], [5, -1], [-2, 4]], 2))
