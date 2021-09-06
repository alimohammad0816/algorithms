"""
    bead sort
        [4, 7, 9, 2, 3, 6, 7] ==> [2, 3, 5, 6, 7, 7, 9]
"""


def bead_sort(sequence: list):
    if any(not isinstance(x, int) or x < 0 for x in sequence):
        raise TypeError("sequence must be list of non-negative integers")
    
    for _ in sequence:
        for i, (upper, lower) in enumerate(zip(sequence, sequence[1:])):
            if upper > lower:
                sequence[i] -= upper - lower
                sequence[i + 1] += upper - lower
    
    return sequence


print(bead_sort([4, 7, 9, 2, 3, 6, 7]))
