def power(x: float, n: int) -> float:
    """
    Implement pow(x, n), which calculates x raised to the power n

    Args:
        x: input float
        n: integer number

    Returns:
        x raised to the power n
    """
    if n == 0:
        return 1
    if x == 0:
        return 0

    val = power(x, int(n / 2))  # to handle -ve power
    val *= val

    if n % 2 != 0:
        return val * x if n > 0 else val * (1/x)  # to handle -ve power
    else:
        return val


if __name__ == "__main__":
    print(power(2.00000, 10))
    print(power(2.10000, 3))
    print(power(2.00000, -2))
    print(power(0.00001, 2147483647))
    print(power(34.00515, -3))
    print(power(0.44528, 0))
    print(power(0, 4))
