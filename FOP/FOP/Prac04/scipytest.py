import matplotlib.pyplot as plt
import numpy as np

from scipy import ndimage
from scipy import misc

face = misc.face (gray=True)
plt.imshow(face)
plt.imshow(face,cmap=plt.cm.gray)


