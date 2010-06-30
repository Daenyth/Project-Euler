#!/usr/bin/env python

from daentools.primes import primes

def problem_ten():
    """
    Find the sum of all the primes below two million.
    """
    limit = 2000000
    return sum(primes(limit))

if __name__ == '__main__':
    print problem_ten()
