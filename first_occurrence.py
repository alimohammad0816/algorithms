"""
    frist occurrence
    [2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 4 ==> 5
"""


def first_occurrence(array, element):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if low == high:
            break
        elif array[mid] < element:
            low = mid + 1
        else:
            high = mid

    if array[low] ==  element:
        return low


print(first_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 4))