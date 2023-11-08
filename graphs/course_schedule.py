from typing import List


def course_schedule(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi
    first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return true if you can finish all courses. Otherwise, return false.

    Args:
        numCourses: number of courses you have to take
        prerequisites: an array where prerequisites[i] = [ai, bi]; representing you must take bi first before taking ai

    Returns:
        true if you can finish all courses, otherwise false
    """
    visited = set()
    pre_req_adj_list = [set() for _ in range(numCourses)]

    for course, pre_req in prerequisites:
        pre_req_adj_list[course].add(pre_req)
    print(pre_req_adj_list)

    def dfs(curr_course):
        if len(pre_req_adj_list[curr_course]) == 0:
            return True

        if curr_course in visited:
            return False

        visited.add(curr_course)
        for pre_req_course in pre_req_adj_list[curr_course]:
            if not dfs(pre_req_course):
                return False

        # visited.remove(curr_course)   # not required if the first base condition is to check for no pre-requisites
        pre_req_adj_list[curr_course] = set()
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False

    return True


if __name__ == '__main__':
    print(course_schedule(2, [[1, 0]]))
    print(course_schedule(2, [[1, 0], [0, 1]]))
    print(course_schedule(1, []))
    print(course_schedule(2, []))
    print(course_schedule(5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]))
