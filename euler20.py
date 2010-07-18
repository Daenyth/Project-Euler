#!/usr/bin/env python

from daentools.mathutils import factorial

def problem_20():
    """
    Find the sum of the digits in the number 100!
    """
    return sum(map(int,list(str(factorial(100)))))

if __name__ == '__main__':
    print problem_20()
