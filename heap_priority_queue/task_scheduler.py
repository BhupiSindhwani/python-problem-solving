import heapq
from collections import deque
from typing import List


def task_scheduler(tasks: List[str], n: int) -> int:
    """
    Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a
    different task. Tasks could be done in any order. Each task is done in one unit of time.
    For each unit of time, the CPU could complete either one task or just be idle.

    However, there is a non-negative integer n that represents the cooldown period between two same tasks
    (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

    Return the least number of units of times that the CPU will take to finish all the given tasks.

    Args:
        tasks: an array of characters representing the tasks a CPU needs to do
        n: non-negative integer that represents the cooldown period b/w two same tasks

    Returns:
        the least number of units of times that the CPU will take to finish all the given tasks
    """
    # Task count
    task_count = {}
    for task in tasks:
        task_count[task] = task_count.get(task, 0) + 1

    # Build Heap
    task_items = [count * -1 for count in task_count.values()]
    heapq.heapify(task_items)

    # Doubly ended queue to maintain the tasks
    task_queue = deque()

    # Schedule tasks
    time_units = 0
    while task_items or task_queue:
        time_units += 1
        if task_items:
            cnt = heapq.heappop(task_items)
            if cnt + 1 < 0:
                task_queue.append((cnt + 1, time_units + n))
        if task_queue and task_queue[0][1] == time_units:
            heapq.heappush(task_items, task_queue.popleft()[0])

    return time_units


if __name__ == "__main__":
    print(task_scheduler(["A", "A", "A", "B", "B", "B"], 2))
    print(task_scheduler(["A", "A", "A", "B", "B", "B"], 0))
    print(task_scheduler(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
