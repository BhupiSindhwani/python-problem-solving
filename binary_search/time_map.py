"""
Design a time-based key-value data structure that can store multiple values for the same key
at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key with the value at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was called previously,
with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated
with the largest timestamp_prev. If there are no values, it returns "".
"""
import collections


class TimeMap:

    def __init__(self):
        self._map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self._map[key]
        left, right = 0, len(values) - 1
        max_time = 0
        found = False
        while left <= right:
            mid = (left + right) // 2
            if timestamp >= values[mid][0]:
                found = True
                max_time = max(max_time, mid)
                left = mid + 1
            else:
                right = mid - 1

        return values[max_time][1] if found else ""


if __name__ == "__main__":
    # timeMap = TimeMap()
    # timeMap.set("foo", "bar", 1)     # store the key "foo" and value "bar" along with timestamp = 1.
    # print(timeMap.get("foo", 1))     # return "bar"
    # print(timeMap.get("foo", 3))     # return "bar", since there is no value corresponding to foo at timestamp 3 and
    # # timestamp 2, then the only value is at timestamp 1 is "bar".
    # timeMap.set("foo", "bar2", 4)    # store the key "foo" and value "bar2" along with timestamp = 4.
    # print(timeMap.get("foo", 5))     # return "bar2"
    # print(timeMap.get("foo", 4))     # return "bar2"

    timeMap = TimeMap()
    timeMap.set("love", "high", 10)
    timeMap.set("love", "low", 20)
    print(timeMap.get("love", 5))
    print(timeMap.get("love", 10))
    print(timeMap.get("love", 15))
    print(timeMap.get("love", 20))
    print(timeMap.get("love", 25))
