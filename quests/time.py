#!/bin/python3

import timeit
import sys


def repCount(string):
	for l in string:
		if string.count(l) > 1:
			return l

string = 'asdfghjklşi,qwertyuıopğüzxcvbnmöç.h'
print('string: ', string)
result = repCount(string)
print('1st repeated letter: ', result)


# Time complexity:
tcode = """
def repCount(string):
	for l in string:
		if string.count(l) > 1:
			return l

string = 'asdfghjklşi,qwertyuıopğüzxcvbnmöç.h'
repCount(string)
"""

print('min time: ', min(timeit.repeat(stmt=tcode, repeat=10)), 'second')
print('max time: ', max(timeit.repeat(stmt=tcode, repeat=10)), 'second')

# Space complexity:

print('space usage: ', sys.getsizeof(result), 'bytes')