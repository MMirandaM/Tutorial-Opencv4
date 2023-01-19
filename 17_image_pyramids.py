import cv2
import numpy as np

img = cv2.imread('./data/lena.jpg')
lr_1 = cv2.pyrDown(img)
lr_2 = cv2.pyrDown(lr_1)

hr_2 = cv2.pyrUp(lr_2)
hr_1 = cv2.pyrUp(hr_2)

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('Upper Level Gausian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
	gaussian_extended = cv2.pyrUp(gp[i])
	laplacian = cv2.subtract(gp[i-1], gaussian_extended)
	cv2.imshow(str(i), laplacian)

cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imshow('Original Image', img)
# cv2.imshow('pyrDown 1 Image', lr_1)
# cv2.imshow('pyrDown 2 Image', lr_2)
# cv2.imshow('pyrUp 2 Image', hr_2)
# cv2.imshow('pyrUp 1 Image', hr_1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()