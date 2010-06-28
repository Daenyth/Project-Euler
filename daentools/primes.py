#!/usr/bin/env python

from math import sqrt, ceil, log
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
    for prime in primes(n):
        while n % prime == 0:
            yield prime
            n /= prime
        if n == 1: break

def approx_nth_prime(n):
    """
    Return an approximation of the nth prime number

    See http://en.wikipedia.org/wiki/Prime_number_theorem
    """
    return n * log(n)

def gen_primes():
    """
    Generate an infinite sequence of prime numbers.

    See http://stackoverflow.com/questions/1628949/to-find-first-n-prime-numbers-in-python/2212923#2212923
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

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
