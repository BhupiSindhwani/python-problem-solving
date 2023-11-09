from typing import List


def course_schedule(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first
    if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return the ordering of courses you should take to finish all courses. If there are many valid answers,
    return any of them. If it is impossible to finish all courses, return an empty array.

    Args:
        numCourses: number of courses you have to take
        prerequisites: an array where prerequisites[i] = [ai, bi]; representing you must take bi first before taking ai

    Returns:
        the ordering of courses to finish all courses, otherwise an empty array
    """
    visited = set()
    result = []
    result_set = set()

    # Capture the list of pre-reqs for each course
    pre_req_list = [set() for _ in range(numCourses)]
    for course, pre_req in prerequisites:
        pre_req_list[course].add(pre_req)

    # recursive call to check for all pre-reqs can be completed
    def dfs(input_course: int) -> bool:
        # Base condition: if the course has been completed:
        if input_course in result_set:
            return True

        # Base Condition: if the course has already been visited, then it's a loop that is not possible to complete
        if input_course in visited:
            return False

        visited.add(input_course)
        for pre_req_course in pre_req_list[input_course]:
            if not dfs(pre_req_course):
                return False

        result.append(input_course)
        result_set.add(input_course)
        return True

    # Iterate through the courses and identify whether it can be completed with it's mentioned pre-reqs
    for crs in range(numCourses):
        if crs not in result_set and not dfs(crs):
            return []
            # return False

    return result
    # return True


if __name__ == '__main__':
    print(course_schedule(2, [[1, 0]]))
    print(course_schedule(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    print(course_schedule(1, []))
    print(course_schedule(2, [[1, 0], [0, 1]]))
    print(course_schedule(2, [[0, 1]]))
