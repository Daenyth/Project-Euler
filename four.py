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
    palindrome = None
    numbers = ["".join(combo) for combo in product([str(x) for x in range(10)], repeat=3)]
    combos = combinations(numbers, 2)

    for x,y in combos:
        x = int(x)
        y = int(y)
        if x is 0 or y is 0: continue
        xy = x * y
        if is_palindrome(xy):
            if xy > palindrome:
                palindrome = xy

    return palindrome

if __name__ == '__main__':
    print problem_four()
