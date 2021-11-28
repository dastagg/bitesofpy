"""Rotate the string by the number supplied."""


def rotate(string, n):
    """Rotate characters in a string.
    Expects string and n (int) for number of characters to move.
    """
    # Use splice method
    # return string[n:] + string[:n]

    # Use deque method
    from collections import deque

    items = deque(string)
    # NOTE: for deque, flip the +/- sign.
    items.rotate(-n)

    # deque works in a list, convert the list to a string.
    return "".join(items)


print(rotate("bob and julian love pybites!", 15))
