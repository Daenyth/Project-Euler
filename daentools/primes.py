#!/usr/bin/env python

from math import sqrt
from memoize import memoized

@memoized
def is_prime(n):
    """
    Checks if a number is prime. Returns True or False
    """
    if x == 2: return True
    if x % 2 == 0: return False
    for x in range(sqrt(n)):
        if x % n == 0: return False

    return True

def prime_factors(n):
    """
    Get the prime factors of n.
    Returns a list of all factors
    """
    pass
