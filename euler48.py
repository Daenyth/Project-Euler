#!/usr/bin/env python

def problem_48():
    """
    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
    """
    return str(sum(map(lambda x: pow(x,x), xrange(1, 1000+1))))[-10:]

if __name__ == '__main__':
    print problem_48()
