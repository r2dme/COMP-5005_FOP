import numpy as np
import matplotlib.pyplot as plt
import sys

def calcheat(r,c):
    result = (b[r-1,c-1]*0.1 + b[r-1,c]*0.1 + b[r-1,c+1]*0.1
                + b[r,c-1]*0.1 + b[r,c]*0.2 + b[r,c+1]*0.1
                + b[r+1,c-1]*0.1 + b[r+1,c]*0.1 +b[r+1,c+1]*0.1)
    return result

size = 10

# read in heat source
hlist = []
fileobj = open(sys.argv[1],'r')
for line in fileobj:
    line_s = line.strip()
    ints= [int(x)for x in line_s.split(',')]
    hlist.append(ints)
fileobj.close()

h = np.array(hlist, dtype=int)
b = h.copy()

print("Heat source:")
print(h)
shortpause = input("Press enter to continue...")

b2 = np.zeros((size,size))

for timestep in range(5):
    for r in range(1, size-1):
        for c in range (1, size-1 ):
            b2[r,c] = calcheat(r,c)

    b2 = np.where(h>b2, h, b2)

    print("Time step: ", timestep)
    print(b2)
    b = b2.copy()    

plt.imshow(b, cmap=plt.cm.hot)
plt.savefig(sys.argv[1].split('.')[0]+'.png')
plt.show()


