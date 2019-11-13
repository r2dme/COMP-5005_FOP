import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals 

t = np.arange(0., 5., 0.2)
t2 = t**2
t3 = t**3

# red dashes, blue squares and green triangles 

plt.title('Multiline')
plt.plot(t, t, 'r--', t, t2, 'bs', t, t3, 'g^') 
plt.show()
