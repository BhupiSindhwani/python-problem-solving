from typing import List


def partition_labels(s: str) -> List[int]:
    """
    You are given a string s. We want to partition the string into as many parts as possible so that each letter
    appears in at most one part.

    Note that the partition is done so that after concatenating all the parts in order,
    the resultant string should be s.

    Return a list of integers representing the size of these parts.

    Args:
        s: input string

    Returns:
        list of integers representing the size of partitions (as many partitions as possible)
    """
    ch_last_idx_map = {}
    result = []

    for idx, ch in enumerate(s):
        ch_last_idx_map[ch] = idx

    curr_size, start = 0, 0
    end = ch_last_idx_map[s[start]]
    while start <= len(s):
        if start <= end:
            curr_size += 1
        else:
            result.append(curr_size)
            curr_size = 1
        end = max(ch_last_idx_map[s[start]], end) if start < len(s) else len(s)
        start += 1
    return result


if __name__ == "__main__":
    print(partition_labels("ababcbacadefegdehijhklij"))
    print(partition_labels("eccbbbbdec"))
    print(partition_labels("caedbdedda"))
