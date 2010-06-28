#!/usr/bin/env python

from functools import partial

def divisible(numerator, denominator):
    """
    Checks if numerator is evenly divisible by denominator.
    Returns True/False
    """
    return numerator % denominator == 0

def skip_count(offset=0, step=1):
    while 1:
        yield offset
        offset += step

def check_divisors(num, factors):
    divcheck = partial(divisible, num)
    return all(map(divcheck, factors))

def greatest_common_factor(a, b):
    """
    Return greatest common factor of nums using Euclid's algorithm
    """
    return (greatest_common_factor(b, a % b) if b else a)

def lowest_common_multiple(nums):
    """
    Return lowest common multiples of nums
    """
    return reduce(lambda a, b: a * b / greatest_common_factor(a, b), nums)
