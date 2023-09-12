def happy_number(n: int) -> bool:
    """
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:

    - Starting with any positive integer, replace the number by the sum of the squares of its digits.
    - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which
    does not include 1.
    - Those numbers for which this process ends in 1 are happy.
    - Return true if n is a happy number, and false if not.

    Args:
        n: an integer

    Returns:
        true if n is a happy number, otherwise false
    """
    # # Using set and recursion
    # elements = set()
    #
    # def get_digits_sum(num: int) -> bool:
    #     nonlocal elements
    #     if num in elements:
    #         return False
    #     if num == 1:
    #         return True
    #
    #     elements.add(num)
    #     curr_sum = 0
    #     while num:
    #         curr_sum += (num % 10) ** 2
    #         num //= 10
    #
    #     return get_digits_sum(curr_sum)
    #
    # return get_digits_sum(n)

    # Using slow and fast pointers

    def get_digits_sum(num: int) -> int:
        curr_sum = 0
        while num:
            curr_sum += (num % 10) ** 2
            num //= 10

        return curr_sum

    slow, fast = n, get_digits_sum(n)

    while slow != fast:
        fast = get_digits_sum(fast)
        fast = get_digits_sum(fast)
        slow = get_digits_sum(slow)

    return True if fast == 1 else False


if __name__ == "__main__":
    print(happy_number(19))
    print(happy_number(2))
