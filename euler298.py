#!/usr/bin/env python

import random

class Memory(object):
    def __init__(self, _):
        self._mem = {}
        self._limit = 5

    def __new__(cls, strategy):
        _subclasses = {
                'longest_missed': LongestMissed,
                'longest_present': LongestPresent }
        return object.__new__(_subclasses[strategy])

    def __contains__(self, num):
        return num in self._mem

    def add(self, num, turn):
        if len(self._mem) >= self._limit:
            self._forget()
        self._update(num, turn)

    def _forget(self):
        lowest = None
        for key in self._mem:
            if lowest is None:
                lowest = key
                continue
            if self._mem[key] < lowest:
                lowest = key

        del self._mem[lowest]

class LongestMissed(Memory):
    def _update(self, num, turn):
        self._mem[num] = turn

class LongestPresent(Memory):
    def _update(self, num, turn):
        if num not in self._mem:
            self._mem[num] = turn

class Player(object):
    def __init__(self, strategy):
        self.score = 0
        self.memory = Memory(strategy)

    def add_point(self):
        self.score += 1

    def remember(self, num):
        self.memory.add(num)

def get_target():
    return random.randrange(1,10+1)

def problem_298():
    """
    Larry and Robin play a memory game involving of a sequence of random
    numbers between 1 and 10, inclusive, that are called out one at a time.
    Each player can remember up to 5 previous numbers. When the called number
    is in a player's memory, that player is awarded a point. If it's not, the
    player adds the called number to his memory, removing another number if his
    memory is full.

    Both players start with empty memories. Both players always add new missed
    numbers to their memory but use a different strategy in deciding which
    number to remove: Larry's strategy is to remove the number that hasn't been
    called in the longest time.  Robin's strategy is to remove the number
    that's been in the memory the longest time.

    Denoting Larry's score by L and Robin's score by R, what is the expected
    value of |L-R| after 50 turns? Give your answer rounded to eight decimal
    places using the format x.xxxxxxxx .
    """

    larry = Player('longest_missed')
    robin = Player('longest_present')

    players = (larry, robin)

    for turn in range(50):
        target = get_target()
        for player in players:
            if target in player.memory:
                player.add_point()
            player.memory.add(target, turn)

    return abs(larry.score - robin.score)

if __name__ == '__main__':
    print problem_298()
