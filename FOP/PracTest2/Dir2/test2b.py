#
# Name : Nishanth Prabu Bharathimohan
# ID   : 19733201
#
# Program Description : Practical test 2 program 
#
#

import matplotlib.pyplot as plt
import numpy as np
import random

numbers = [1, 2, 3, 4, 5, 6]
added = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
counts = np.zeros((2,len(numbers)))
sums = np.zeros((len(added)))

throws = int(input("Enter number of throws..."))

for throw in range(throws):
    throw1 = random.choice(numbers)
    counts[0, throw1 - 1] += 1
    throw2 = random.choice(numbers)
    counts[1, throw2 - 1] += 1
    sums[throw1 - 1 + throw2 - 1] += 1

plt.suptitle('Dice Roll Simulation', fontsize=18)

plt.subplot(131)
plt.ylabel('Count')
plt.bar(numbers, counts[0,:],color='violet')

plt.subplot(132)
plt.xlabel('Dice Roll Value')
plt.bar(numbers, counts[1,:],color='indigo')

plt.subplot(133)
plt.bar(added, sums,color='thistle')


plt.savefig('test2b.png')
plt.show()
