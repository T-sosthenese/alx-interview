#!/usr/bin/python3
"""
Module implementation for determining the least number of copy
and paste operations required to acheive a specific number of
characters starting from 1
"""


def minOperations(n):
    """
    Function that returns the min number of copy-paste operations.
    """
    if n <= 1:
        return 0  # We already have 1 'H' so copy-pasted must be more

    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            n //= factor
            operations += factor
        factor += 1
    return operations
