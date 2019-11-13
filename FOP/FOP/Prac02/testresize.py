import numpy as np

data = np.zeros((2,2,3)) 

data[0,1,2] = 1

data[1,1,1] = 2

print(data)

data.resize(2,6) 

print(data)
