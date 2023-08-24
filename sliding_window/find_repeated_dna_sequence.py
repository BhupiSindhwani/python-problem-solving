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
    # Solution using polynomial rolling hash
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    hash_value = 0
    sequences = set()
    output = set()
    a = 4  # base value

    numbers = [0] * len(s)
    hi_power = pow(a, k - 1)

    for idx, ch in enumerate(s):
        numbers[idx] = mapping[ch]

    for start in range(len(s) - k + 1):
        if start == 0:
            for end in range(k):
                hash_value += numbers[end] * (a ** (k - end - 1))
        else:
            hash_value = ((hash_value - (numbers[start - 1] * hi_power)) * a) + numbers[start + k - 1]
        if hash_value in sequences:
            output.add(s[start: start + k])
        sequences.add(hash_value)

    return output


if __name__ == "__main__":
    print(find_repeated_dna_sequence("AAAAACCCCCAAAAACCCCCC", 8))
    print(find_repeated_dna_sequence("GGGGGGGGGGGGGGGGGGGGGGGGG", 12))
    print(find_repeated_dna_sequence("TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", 10))
    print(find_repeated_dna_sequence("AAAAAACCCCCCCAAAAAAAACCCCCCCTG", 10))
    print(find_repeated_dna_sequence("ATATATATATATATAT", 6))
