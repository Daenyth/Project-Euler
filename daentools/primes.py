#!/usr/bin/env python

from math import sqrt, ceil
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

    for prime in primes(n):
        while n % prime == 0:
            factors.append(prime)

def primes(limit):
    """
    Return a list of primes up to limit using the seive of eratosthenes
    """
    limit = int(ceil(sqrt(limit)))
    num_tab = range(1,limit,2)
    # our table looks like 1,3,5,7,... we change the first
    # to the first prime, 2
    num_tab[0] = 2
    i = 1
    # biggest number in our table
    highestval = num_tab[-1]
    while 1:
        # find first operator in the sieve
        cx = num_tab[i]
        # non working value so move to the next
        if cx is False:
            i += 1
            continue
        # first value to be sieved is always going to be
        # the current number * itself. all the next numbers in
        # that sieve will be larger.
        if cx**2 > limit:
            break
        # strike off - our sieve
        tostrike = []
        for j in xrange(i,len(num_tab)):
            # find the second operator in the sieve
            cy = num_tab[j]
            # non-working value... skip over
            if cy is False:
                continue
            cut = cx*cy
           # outside the sieve's bounds
            if cut > highestval:
                break
            # add to our sieve
            tostrike.append(cut)
        # sieve the values from our number table
        for d in tostrike:
            ind = (d - 1)/2
            num_tab[ind] = False
        # find the highest value in our number table that
        # hasn't been sieved
        hiind = -1
        while num_tab[hiind] == False:
            hiind -= 1
        highestval = num_tab[hiind]

        i += 1
    return [x for x in num_tab if x is not False]
