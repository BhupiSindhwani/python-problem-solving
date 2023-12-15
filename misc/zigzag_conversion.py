def zigzag_conversion(s: str, numRows: int) -> str:
    """
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"

    Args:
        s: input string
        numRows: number of rows for the zigzag pattern

    Returns:
        rewritten string in a zigzag format
    """
    if numRows == 1:
        return s

    result = ""

    for row in range(numRows):
        inc1 = (numRows - 1) * 2
        inc2 = (numRows - row - 1) * 2
        for idx in range(row, len(s), inc1):
            result += s[idx]
            if 0 < row < numRows - 1\
                    and idx + inc2 < len(s):
                result += s[idx + inc2]

    return result


if __name__ == '__main__':
    print(zigzag_conversion("PAYPALISHIRING", 3))
    print(zigzag_conversion("PAYPALISHIRING", 4))
    print(zigzag_conversion("A", 1))
    print(zigzag_conversion("APPLE", 5))
