#
# heat.py
#
import matplotlib.pyplot as plt 
import numpy as np

size = 10
b = np.zeros((size,size))

# Create heat source
for i in range(size):
    b[i,0] = 10
print('\nHEAT DIFFUSION SIMULATION\n') 
print('Initial array...')
print(b)

# Temp array for storing calculations
b2 = np.zeros((size,size))

# Calculate heat diffusion
for timestep in range(5):
    for r in range(1, size-1):
        for c in range (1, size-1 ):
             b2[r,c] = (b[r-1,c-1]*0.1 + b[r-1,c]*0.1 + b[r-1,c+1]*0.1 + b[r,c-1]*0.1+ b[r,c]*0.2 + b[r,c+1]*0.1+ b[r+1,c-1]*0.1 + b[r+1,c]*0.1 + b[r+1,c+1]*0.1)
    for i in range(size): 
        b2[i,0] = 10
    b = b2.copy()

plt.title('Heat Diffusion Simulation') 
plt.imshow(b2, cmap=plt.cm.hot,interpolation = 'bilinear') 
plt.colorbar()
plt.show()
