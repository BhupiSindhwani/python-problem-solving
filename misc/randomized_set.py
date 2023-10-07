"""
Implement the RandomizedSet class:

 - RandomizedSet() Initializes the RandomizedSet object.
 - bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present,
 false otherwise.
 - bool remove(int val) Removes an item val from the set if present. Returns true if the item was present,
 false otherwise.
 - int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one
 element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.
"""
import random


class RandomizedSet:

    def __init__(self):
        self._map = {}
        self._list = []

    def insert(self, val: int) -> bool:
        if val in self._map:
            return False
        self._list.append(val)
        self._map[val] = len(self._list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self._map:
            return False
        idx = self._map[val]
        last_val = self._list[-1]
        self._list[idx] = last_val
        self._list.pop()
        self._map[last_val] = idx
        del self._map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self._list)


if __name__ == "__main__":
    randomizedSet = RandomizedSet()
    print(randomizedSet.insert(0))
    print(randomizedSet.insert(1))
    print(randomizedSet.remove(0))
    # print(randomizedSet.getRandom())
    print(randomizedSet.insert(2))
    print(randomizedSet.remove(1))
    print(randomizedSet.getRandom())
