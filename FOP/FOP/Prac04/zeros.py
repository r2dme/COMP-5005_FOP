#
# Zeros.py - creating and resizing an array
#

import numpy as np

print ('\nZERO ARRAY\n')
zeroarray = np.zeros((3,3,3))

zeroarray[0,0,2]=1
zeroarray[1,1,1]=2
zeroarray[2,2,0]=3

print('Zero array size: ',np.size(zeroarray))
print('Zero array shape: ',np.shape(zeroarray), '\n')
print(zeroarray)

zeroarray.resize((1,27))
print('\nZero array size is: ',np.size(zeroarray))
print('\nZero array shape is: ',np.shape(zeroarray),'\n')
print(zeroarray)

zeroarray.resize((3,9))
print('\nZero array size: ', np.size(zeroarray)) 
print('Zero array shape: ', np.shape(zeroarray),'\n')
print(zeroarray)


