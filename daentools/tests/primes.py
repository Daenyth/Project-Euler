#!/usr/bin/env python

import unittest

from daentools import primes

class IsPrime(unittest.TestCase):
    def test_is_prime(self):
        for p in primes.primes(20000):
            self.assertTrue(primes.is_prime, p)

class Primes(unittest.TestCase):
    def test_primes(self):
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.assertEqual(prime_list, primes.primes(50))

class PrimeFactors(unittest.TestCase):
    def test_prime_factors(self):
        factors = {
            10: set([2,5]),
            20: set([2,2,5]),
            57: set([3,19]),
        }
        for num in factors:
            self.assertEqual(primes.prime_factors(num), factors[num], 'Incorrect factor list for %d' % num)

if __name__ == '__main__':
    unittest.main()
