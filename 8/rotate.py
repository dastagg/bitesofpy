"""Rotate the string by the number supplied."""


def rotate(string, n):
    """Rotate characters in a string.
    Expects string and n (int) for number of characters to move.
    """
    return string[n:] + string[:n]
