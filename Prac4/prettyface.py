#
# prettyface.py
#
import matplotlib.pyplot as plt 
from scipy import ndimage
from scipy import misc

face = misc.face(gray=True) 

plt.imshow(face)
plt.imshow(face, cmap=plt.cm.gray) 
plt.show()
