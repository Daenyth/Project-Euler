#!/usr/bin/env python

def problem_one():
    """
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    def wanted_multiples(x):
        return x % 3 == 0 or x % 5 == 0
    return sum(filter(wanted_multiples, range(1000)))

if __name__ == '__main__':
    print problem_one()
