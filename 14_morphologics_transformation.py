import matplotlib.pyplot as plt
import cv2
import numpy as np 

img = cv2.imread('./smarties.png', cv2.IMREAD_GRAYSCALE) # or (...., 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# mask = cv2.imread('./j.png', cv2.IMREAD_GRAYSCALE)

kernal = np.zeros((5,5), np.uint8)
dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) # erosion -> dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal) # dilation -> erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
th  = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

titles = ['mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [mask, dilation, erosion, opening, closing, mg, th]

for i in range(len(images)):
	plt.subplot(2,4	,i+1)
	plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks([]), plt.yticks([])

plt.show()