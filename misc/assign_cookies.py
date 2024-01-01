from collections import defaultdict
from typing import List


def assign_cookies(g: List[int], s: List[int]) -> int:
    """
    Assume you are an awesome parent and want to give your children some cookies.
    But, you should give each child at most one cookie.

    Each child 'i' has a greed factor g[i], which is the minimum size of a cookie that the child
    will be content with; and each cookie 'j' has a size s[j]. If s[j] >= g[i], we can assign the
    cookie j to the child i, and the child i will be content.

    Your goal is to maximize the number of your content children and output the maximum number.

    Args:
        g: an array representing the greed factor for each child
        s: an array representing the cookie size

    Returns:
        the maximum number of content children
    """
    g.sort()
    s.sort()

    gd, sz = 0, 0

    while gd < len(g) and sz < len(s):
        if g[gd] <= s[sz]:
            gd += 1
        sz += 1

    return gd


if __name__ == '__main__':
    print(assign_cookies([1, 2, 3], [1, 1]))
    print(assign_cookies([1, 2], [1, 2, 3]))
