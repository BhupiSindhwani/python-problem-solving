"""
Design a data structure that follows the constraints of Least Recently Used (LRU) cache.

Implement the LRUCache class:

- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""


class ListNode:

    def __init__(self, val: (int, int), prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key: int, val: pointer to the Node
        self.lru_head, self.lru_tail = ListNode(0, 0), ListNode(0, 0)
        self.lru_head.next, self.lru_tail.prev = self.lru_tail, self.lru_head

    @staticmethod
    def remove(node):
        node_prev, node_next = node.prev, node.next
        node_prev.next, node_next.prev = node_next, node_prev

    def insert(self, node) -> None:
        tail_prev, tail_next = self.lru_tail.prev, self.lru_tail
        tail_prev.next, node.prev = node, tail_prev
        node.next, tail_next.prev = tail_next, node

    @staticmethod
    def print_list(node):
        curr = node
        while curr.next:
            print(f"{curr.val}->", end="")
            curr = curr.next
        print(curr.val)
        while curr:
            print(f"{curr.val}->", end="")
            curr = curr.prev
        print()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            LRUCache.remove(node)
            self.insert(node)
            return node.val[1]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            LRUCache.remove(self.cache[key])
        new_node = ListNode((key, value))
        self.cache[key] = new_node
        self.insert(new_node)
        if len(self.cache) > self.capacity:
            del self.cache[self.lru_head.next.val[0]]
            LRUCache.remove(self.lru_head.next)


if __name__ == "__main__":
    # lRUCache = LRUCache(2)
    # lRUCache.put(1, 0)
    # lRUCache.put(2, 2)
    # print(lRUCache.get(1))
    # lRUCache.put(3, 3)
    # print(lRUCache.get(2))
    # lRUCache.put(4, 4)
    # print(lRUCache.get(1))
    # print(lRUCache.get(3))
    # print(lRUCache.get(4))

    lRUCache = LRUCache(2)
    print(lRUCache.get(2))
    lRUCache.put(2, 6)
    print(lRUCache.get(1))
    lRUCache.put(1, 5)
    lRUCache.put(1, 2)
    print(lRUCache.get(1))
    print(lRUCache.get(2))
