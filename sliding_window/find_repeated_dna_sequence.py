def find_repeated_dna_sequence(s: str, k: int) -> set:
    """
    Given a string, s, that represents a DNA subsequence, and a number k,
    return all the contiguous subsequences (substrings) of length k that occur more than once in the string.

    The DNA sequence is composed of a series of nucleotides abbreviated as A, C, G, and T.
    For example, ACGAATTCCG is a DNA sequence.

    The order of the returned subsequences does not matter.
    If no repeated substring is found, the function should return an empty set.

    Args:
        s: input string representing a DNA sequence
        k: an integer

    Returns:
        all the contiguous subsequences (substrings) of length k that occur more than one in the input string
    """
    start, end = 0, 0

    sequences = set()
    output = set()

    while end < len(s):
        if end - start + 1 <= k:
            end += 1
        else:
            if s[start: end] in sequences:
                output.add(s[start: end])
            else:
                sequences.add(s[start: end])
            end += 1
            start += 1

    return output


if __name__ == "__main__":
    print(find_repeated_dna_sequence("AAAAACCCCCAAAAACCCCCC", 8))
    print(find_repeated_dna_sequence("GGGGGGGGGGGGGGGGGGGGGGGGG", 12))
    print(find_repeated_dna_sequence("TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", 10))
    print(find_repeated_dna_sequence("AAAAAACCCCCCCAAAAAAAACCCCCCCTG", 10))
    print(find_repeated_dna_sequence("ATATATATATATATAT", 6))
