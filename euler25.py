#!/usr/bin/env python

from itertools import count

from daentools.sequences import fib

def problem_25():
    """
    What is the first term in the Fibonacci sequence to contain 1000 digits?
    """
    digits = lambda x: len(str(x))
    for n in count(1):
        num = fib(n)
        if digits(num) < 1000: continue
        return n

if __name__ == '__main__':
    print problem_25()
