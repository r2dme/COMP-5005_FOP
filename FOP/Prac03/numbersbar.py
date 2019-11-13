#
# numbersbar.py: Read in ten numbers and give sum, min, max and mean. Also plot the numbers as a bar chart
#

import numpy as np
import matplotlib.pyplot as plt

numarray = np.zeros(10) 

# creates an empty array 10 elements long

print('Enter ten numbers...')

for i in range(len(numarray)): 
	print('Enter a number (', i, ')...') 
	numarray[i] = int(input())

print('Total is ', numarray.sum())
print('Min number is ',numarray.min(),'\nMax number is ',numarray.max())
print('Average is ',numarray.mean())

# plot


plt.title('Numbers Bar Chart') 
plt.xlabel('Index')
plt.ylabel('Number')
plt.bar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], numarray, 0.9, color='purple')

plt.show()
