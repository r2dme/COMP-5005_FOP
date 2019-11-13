import numpy as np;

a = np.array([[1,2],[3,4]])

print (a)

print (np.shape(a))

c = a.reshape(1,4)

print (c)

print (c[0,0])

row,col = 0,0

while row<len(a[:,0]):
    while col<len(a[0,:]):
        print ('Element [',row,',',col,'] is: ', a[row,col])
        col = col+1
    row = row+1
    col=0




