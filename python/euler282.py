#!/usr/bin/env python

from daentools.mathutils import ackermann

def problem_282():
    """
    Find (Sigma A(n,n) for n=0->6) mod 14**8
    """
    sigma = sum(map(lambda n: ackermann(n,n), xrange(6+1)))
    return sigma % 14 ** 8

if __name__ == '__main__':
    print problem_282()
