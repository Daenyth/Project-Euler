#!/usr/bin/env python

import string


def letter_value(letter):
    """
    Get the point value for a letter
    """
    return string.ascii_lowercase.index(letter) + 1

def name_value(name):
    """
    Get the point value for a name
    """
    return sum(letter_value(l) for l in name.lower())

def problem_22(filename):
    """
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text
    file containing over five-thousand first names, begin by sorting it into
    alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a
    name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is
    worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
    obtain a score of 938  53 = 49714.

    What is the total of all the name scores in the file?
    """
    with open(filename) as f:
        names = sorted([n for n in f.readline().replace('"', '').split(',')])

    name_points = {name: name_value(name) * (i+1) for i, name in enumerate(names)}

    return sum(name_points.values())

if __name__ == '__main__':
    print(problem_22('22-names.txt'))
