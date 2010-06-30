#!/usr/bin/env python

from daentools.math import lowest_common_multiple

def problem_five():
    """
    2520 is the smallest number that can be divided by each of the
    numbers from 1 to 10 without any remainder.

    Return the smallest positive number that is evenly divisible by
    all of the numbers from 1 to 20.
    """
    return lowest_common_multiple(xrange(1, 20+1))

if __name__ == '__main__':
    print problem_five()
