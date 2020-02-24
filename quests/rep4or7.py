#!/bin/python3

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
result = print(arr4or7(arr))
result

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

time_comp = timeit.repeat(stmt=tcode, repeat=10)
print('min time: ', min(time_comp), 'second')
print('max time: ', max(time_comp), 'second')

# Space complexity:
print('space usage: ', sys.getsizeof(result) + sys.getsizeof(arr), 'bytes')
