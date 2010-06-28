#!/usr/bin/env python

import operator as op

def problem_six():
    """
    Find the difference between the sum of the squares of the first
    one hundred natural numbers and the square of the sum.

    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first
    ten natural numbers and the square of the sum is 3025  385 = 2640.
    """
    square = lambda x: pow(x,2)
    sum_of_squares = reduce(op.add, map(square, xrange(1,100+1)))
    square_of_sum = square(reduce(op.add, xrange(1,100+1)))

    return square_of_sum - sum_of_squares

if __name__ == '__main__':
    print problem_six()
