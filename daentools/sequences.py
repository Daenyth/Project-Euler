#!/usr/bin/env python

from memoize import memoized
from itertools import count

@memoized
def fib(n):
    """
    Return the nth fibonacci number
    """
    if n < 2: return n
    return fib(n-1) + fib(n-2)

def triangle_numbers(limit=None):
    """
    The sequence of triangle numbers is generated by adding the natural
    numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 +
    6 + 7 = 28.

    Takes an optional limit of the nth last number to yield
    """
    total = 0
    for num in count():
        total += num
        yield total
        if num == limit:
            break
