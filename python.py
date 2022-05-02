# Python program to illustrate
# arithmetic operation of
# bitwise AND of two images
	
# organizing imports
import cv2
import numpy as np
	
# path to input images are specified and
# images are loaded with imread command
img1 = cv2.imread('BOOL11.gif')
img2 = cv2.imread('BOOL12.gif')

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 127, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# cv2.bitwise_and is applied over the
# image inputs with applied parameters
dest_and = cv2.bitwise_or(img1, img2, mask = mask)

# the window showing output image
# with the Bitwise AND operation
# on the input images
cv2.imshow('Bitwise And', dest_and)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
