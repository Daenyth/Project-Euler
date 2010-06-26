#!/usr/bin/env python

from daentools.primes import prime_factors

def problem_three():
    """
    Return the largest prime factor of the number 600851475143
    """
    return max(prime_factors(600851475143))

if __name__ == '__main__':
    print problem_three()
