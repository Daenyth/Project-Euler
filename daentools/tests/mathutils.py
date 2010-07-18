#!/usr/bin/env python

import unittest

from daentools import mathutils

class Factors(unittest.TestCase):
    def test_factors(self):
        factors = {
            200013: set([(3,1), (11,2), (19,1), (29,1)]),
            10: set([(2,1), (5,1)]),
            20: set([(2,2), (5,1)]),
            40: set([(2,3), (5,1)]),
            937: set([(937,1)]),
        }

        for num in factors:
            self.assertEqual(factors[num], set(mathutils.factors(num)))

if __name__ == '__main__':
    unittest.main()
