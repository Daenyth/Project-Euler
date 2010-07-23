#!/usr/bin/env python

from itertools import product, combinations

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def problem_four():
    """
    Find the largest palindrome made from the product of two 3-digit numbers.

    A palindromic number reads the same both ways.
    The largest palindrome made from the product of
    two 2-digit numbers is 9009 = 91 * 99.
    """
    numbers = [x*y for x in xrange(100,999+1) for y in xrange(100,999+1)]
    return max(filter(is_palindrome, numbers))

if __name__ == '__main__':
    print problem_four()
