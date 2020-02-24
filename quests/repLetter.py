#!/bin/python3

import time
import timeit
import sys


def repLetter(string):
	for l in string:
		if string.count(l) > 1:
			return l

string = 'Intergalactic'
print('string: ', string)
result = repLetter(string)
t1 = time.clock()
result
t2 = time.clock()
print('1st repeated letter: ', result)

# Time complexity:
tcode = """
def repLetter(string):
	for l in string:
		if string.count(l) > 1:
			return l

string = 'Intergalactic'
repLetter(string)
"""

time_comp = timeit.repeat(stmt=tcode, repeat=10)
print('min time: ', min(time_comp), 'second')
print('max time: ', max(time_comp), 'second')
print('actual duration: ', t2 - t1, 'second')

# Space complexity:
print('space usage: ', sys.getsizeof(result) + sys.getsizeof(string), 'bytes')