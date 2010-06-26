#!/usr/bin/env python

from itertools import count, takewhile

from daentools.fibonacci import fib

def problem_two(limit=4000000):
    """
    Find the sum of all the even-valued terms in the fibonacci sequence
    which do not exceed four million.
    """
    even_fibs = (fib(n) for n in count() if fib(n) % 2 == 0)
    return sum(takewhile(lambda x: x < limit, even_fibs))

if __name__ == '__main__':
    print problem_two()
