#!/usr/bin/env python

from daentools.math import is_pythagorean
from daentools.misc import first

def problem_nine():
    """
    A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    target = 1000
    combinations = [(a,b,target-b-a) for b in xrange(1, target/2) for a in xrange(b,target/2)]
    triples = filter(is_pythagorean, combinations)
    a,b,c = first(filter(lambda t: sum(t) == target, triples))
    return a*b*c

if __name__ == '__main__':
    print problem_nine()
