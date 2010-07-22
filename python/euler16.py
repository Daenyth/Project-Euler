#!/usr/bin/env python


def problem_16():
    """
    2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2**1000?
    """
    return sum(map(int,list(str(2**1000))))

if __name__ == '__main__':
    print problem_16()
