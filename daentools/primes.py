#!/usr/bin/env python

from math import sqrt
from memoize import memoized

@memoized
def is_prime(n):
    """
    Checks if a number is prime. Returns True or False
    """
    if n == 2: return True
    if n % 2 == 0: return False
    for x in range(sqrt(n)):
        if x % n == 0: return False

    return True

def prime_factors(n):
    """
    Get the prime factors of n.
    Returns a list of all factors
    """
    if n == 1: return [1]

    factors = []

    for prime in gen_primes(n):
        while n % prime == 0:
            factors.append(prime)
