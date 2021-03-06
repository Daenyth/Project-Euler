#!/usr/bin/env python

from functools import partial
import operator as op

from primes import prime_factors
from memoize import memoized

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
    Given a number, return a list of all factors as (prime, exponent) tuples
    """
    factors = {}
    try:
        for factor in prime_factors(number):
            try:
                factors[factor] += 1
            except KeyError:
                factors[factor] = 1
    except TypeError:
        # prime_numbers() is None
        pass # No factors but itself

    if len(factors) == 0: return [(number, 1)]
    return [(prime, exp) for (prime, exp) in factors.items()]

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

@memoized
def ackermann(m, n):
    while m >= 4:
        if n == 0:
            n = 1
        else:
            n = ackermann(m, n - 1)

    if m == 3:
        return 2 ** (n + 3) - 3
    if m == 2:
        return 2 * n + 3
    if m == 1:
        return n + 2
    return n + 1

def hyper(base, a, b):
    if base == 0:
        return b + 1
    if b == 0:
        if base == 1:
            return a
        if base == 2:
            return 0
        if base >= 3:
            return 1
    return hyper(base - 1, a, hyper(base, a, b - 1))
