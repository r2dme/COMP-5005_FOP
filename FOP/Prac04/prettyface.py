#
# prettyface.py
#
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from scipy import misc

face = misc.face(gray=True)

plt.imshow(face)
plt.show()
plt.imshow(face,cmap=plt.cm.gray)
plt.show()
plt.imshow(face,cmap=plt.cm.gray_r)


# shifting

shifted_face=ndimage.shift(face,(50,50))
plt.imshow(shifted_face)
plt.show()

#rotating
rotated_face=ndimage.rotate(face,(10,20))
plt.imshow(rotated_face)
plt.show()


#cropping
cropped_face = face[100:-100,100:-100]
plt.imshow(cropped_face)
plt.show()



