#!/usr/bin/env python

import unittest
import operator as op

from daentools import primes

class IsPrime(unittest.TestCase):
    def test_is_prime(self):
        for p in primes.primes(20000):
            self.assertTrue(primes.is_prime(p), 'Prime %d fails prime check' % p)

class Primes(unittest.TestCase):
    def test_primes(self):
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.assertEqual(prime_list, primes.primes(50))

class PrimeFactors(unittest.TestCase):
    def test_prime_factors(self):
        # Loop downwards so we don't have to keep re-seiving the prime list
        for num in xrange(10000,2,-1):
            factors = primes.prime_factors(num)
            if not factors:
                self.assertTrue(primes.is_prime(num), 'No factor list returned for non-prime %d' % num)
                continue
            product = reduce(op.mul, factors)

            self.assertEqual(product, num, 'Incorrect factor list for %d: (%s) = %d' % (num, "*".join(map(str, factors)), product))

if __name__ == '__main__':
    unittest.main()
