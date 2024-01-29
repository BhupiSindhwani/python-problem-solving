"""
Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue
(push, peek, pop, and empty).

Implement the MyQueue class:

- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
- You must use only standard operations of a stack, which means only
push to top, peek/pop from top, size, and is empty operations are valid.
"""


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def stack_unload(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            self.stack_unload()
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            self.stack_unload()
        return self.stack2[-1]

    def empty(self) -> bool:
        return max(len(self.stack1), len(self.stack2)) == 0


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())
