"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

 - MyHashMap() initializes the object with an empty map.
 - void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map,
 update the corresponding value.
 - int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping
 for the key.
 - void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
"""


# # Solution using fixed array
# class MyHashMap:
#
#     def __init__(self):
#         self._map = [-1] * ((10 ** 6) + 1)
#
#     def put(self, key: int, value: int) -> None:
#         self._map[key] = value
#
#     def get(self, key: int) -> int:
#         return self._map[key] if key < len(self._map) else -1
#
#     def remove(self, key: int) -> None:
#         if key < len(self._map):
#             self._map[key] = -1


# Solution using dynamic array and linked list
class ListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1009
        self._map = [None] * self.size

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        dummy = ListNode(0, 0)
        if self._map[idx]:
            dummy.next = self._map[idx]
            prev, curr = dummy, dummy.next
            while curr:
                if curr.key == key:
                    curr.value = value
                    return
                prev, curr = curr, curr.next
            prev.next = ListNode(key, value)
        else:
            self._map[idx] = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % self.size
        if self._map[idx]:
            curr = self._map[idx]
            while curr:
                if curr.key == key:
                    return curr.value
                curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.size
        dummy = ListNode(0, 0)
        if self._map[idx]:
            dummy.next = self._map[idx]
            prev, curr = dummy, dummy.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                prev, curr = curr, curr.next
        self._map[idx] = dummy.next


if __name__ == "__main__":
    myHashMap = MyHashMap()
    myHashMap.put(1, 1)
    myHashMap.put(2, 2)
    print(myHashMap.get(1))
    print(myHashMap.get(3))
    myHashMap.put(2, 1)
    print(myHashMap.get(2))
    myHashMap.remove(2)
    print(myHashMap.get(2))

    myHashMap = MyHashMap()
    myHashMap.remove(2)
    myHashMap.put(3, 11)
    myHashMap.put(4, 13)
    myHashMap.put(15, 6)
    myHashMap.put(6, 15)
    myHashMap.put(8, 8)
    myHashMap.put(11, 0)
    print(myHashMap.get(11))
    myHashMap.put(1, 10)
    myHashMap.put(12, 14)
