"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self._min_list = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self._min_list:
            self._min_list.append(val)
        elif val <= self._min_list[-1]:
            self._min_list.append(val)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self._min_list[-1]:
            self._min_list.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min_list[-1]


if __name__ == "__main__":
    minstack = MinStack()
    minstack.push(-2)
    minstack.push(0)
    minstack.push(-3)
    print(minstack.getMin())  # return -3
    minstack.pop()
    print(minstack.top())  # return 0
    print(minstack.getMin())  # return -2
