#!/bin/python3

import time
import timeit
import sys


def arr4or7(arr):
	for i in range(len(arr)):
		if arr[i] % 28 == 0:
			arr[i] = 'fs'
		elif arr[i] % 4 == 0:
			arr[i] = 'f'
		elif arr[i] % 7 == 0:
			arr[i] = 's'
	print(arr)
	return 1

arr = [i for i in range(1, 101)]
result = arr4or7(arr)

t1 = time.clock()
result
t2 = time.clock()

# Time complexity:
tcode = """
def arr4or7(arr):
	for i in range(len(arr)):
		if arr[i] % 28 == 0:
			arr[i] = 'fs'
		elif arr[i] % 4 == 0:
			arr[i] = 'f'
		elif arr[i] % 7 == 0:
			arr[i] = 's'
	return 1

arr = [i for i in range(1, 101)]
arr4or7(arr)
"""

time_comp = timeit.repeat(stmt=tcode, repeat=2)
print('min time: ', min(time_comp), 'second')
print('max time: ', max(time_comp), 'second')
print('actual duration: ', t2 - t1, 'sec')

# Space complexity:
print('space usage: ', sys.getsizeof(result) + sys.getsizeof(arr), 'bytes')