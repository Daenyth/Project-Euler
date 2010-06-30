#!/usr/bin/env python

from itertools import islice

def skip_count(offset=0, step=1):
    while 1:
        yield offset
        offset += step

def first(list):
    return list[0]

def nth(iterable, n, default=None):
    """
    Returns the nth item or a default value
    """
    return next(islice(iterable, n, None), default)

def flatten(input):
    """
    Flatten a nested list/tuple structure and return a simple list

    Given [(a,b),c], return [a,b,c]
    """
    ret = []
    if not isinstance(input, (list, tuple)):
        return [input]
    for i in input:
        if isinstance(i, (list, tuple)):
            ret.extend(flatten(i))
        else:
            ret.append(i)
    return ret
