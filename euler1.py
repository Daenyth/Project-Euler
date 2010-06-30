#!/usr/bin/env python

import sys

import unittest

class ProblemOneTest(unittest.TestCase):
    def test_me(self):
        self.assertEquals(problem_one(),233168)

def problem_one():
    """
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    def wanted_multiples(x):
        return x % 3 == 0 or x % 5 == 0
    return sum(filter(wanted_multiples, range(1000)))

if __name__ == '__main__':
    print "Problem 1 possible answer: %d" % problem_one()
    sys.exit(unittest.main())
