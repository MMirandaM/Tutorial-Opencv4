import matplotlib.pyplot as plt
import cv2
import numpy as np 

# filter, blur
# img = cv2.imread('./data/opencv-logo.png') 

# gaussian, median
img = cv2.imread('./data/noise_salt_and_pepper.png')


# img = cv2.imread('./data/lena.jpg')


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((6,6), np.float32)/36
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5,5))
gblur = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Convolution', 'Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(len(images)):
	plt.subplot(2,3,i+1)
	plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks([]), plt.yticks([])

plt.show()