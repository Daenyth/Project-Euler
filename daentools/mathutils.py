#!/usr/bin/env python

import math

from functools import partial

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

def factors(number):
    """
    Given a number, return a list of all possible integer factors.

    Note that this returns all factors, not just primes.
    """
    factors = set([1, number])
    for divisor in xrange(2, int(math.ceil(math.sqrt(number)))):
        if divisible(number, divisor):
            factors.add(divisor)

    return factors

def divisible(numerator, denominator):
    """
    Checks if numerator is evenly divisible by denominator.
    Returns True/False
    """
    return numerator % denominator == 0

def is_pythagorean(triple):
    """
    Checks if 3-tuple (a,b,c) is a pythagorean triplet
    a^2 + b^2 = c^2
    Returns True/False
    """
    a,b,c = triple
    return a**2 + b**2 == c**2

def pythagorean_triple_vii(n):
    """
    Given n, create the corresponding pythagorean triple using formula VII as described in
    http://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples

    Creates a triple where c = b + 1

    Returns ((a,b),c)
    """
    a = (2 * n * n) + (2 * n)
    b = (2 * n) + 1
    c = max(a,b) + 1
    return ((a,b),c)

def pythagorean_triples(n=1,limit=None):
    """
    Generate a series of pythagorean triples beginning at n or 1 and
    ending at an optional limit
    """
    pythagorean_triple = pythagorean_triple_vii
    while n != limit:
        triple = pythagorean_triple(n)
        yield triple
        n += 1

