#!/usr/bin/env python

from memoize import memoized

@memoized
def fib(n):
    """
    Return the nth fibonacci number
    """
    if n < 2: return n
    return fib(n-1) + fib(n-2)

def triangle_numbers():
    pass
