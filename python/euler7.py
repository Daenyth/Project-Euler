#!/usr/bin/env python

from daentools.primes import gen_primes
from daentools.misc import nth

def problem_seven():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.

    What is the 10001st prime number?
    """
    return nth(gen_primes(), 10000)

if __name__ == '__main__':
    print problem_seven()
