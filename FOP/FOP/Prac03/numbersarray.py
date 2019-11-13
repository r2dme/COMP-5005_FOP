#
# numbersarray.py: Read in ten numbers and give sum, min, max and mean
#

import numpy as np

numarray = np.zeros(10) 

# creates an empty array 10 elements long

print('Enter ten numbers...')

for i in range(len(numarray)): 
	print('Enter a number (', i, ')...') 
	numarray[i] = int(input())

print('Total is ', numarray.sum())
print('Min number is ',numarray.min(),'\nMax number is ',numarray.max())
print('Average is ',numarray.mean())


