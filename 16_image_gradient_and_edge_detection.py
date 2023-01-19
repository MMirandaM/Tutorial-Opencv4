import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread('./data/messi5.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('./data/sudoku.png', cv2.IMREAD_GRAYSCALE)

# Grandiente de Laplace
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, dx=1, dy=0)
sobelY = cv2.Sobel(img, cv2.CV_64F, dx=0, dy=1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelXY = cv2.bitwise_or(sobelX, sobelY)

canny = cv2.Canny(img, 100, 200)

titles = ['image', 'Laplacian', 'SobelX', 'SobelY', 'SobelXY', 'Canny']
images = [img, lap, sobelX, sobelY, sobelXY, canny]

for i in range(len(titles)):
    plt.subplot(2,3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()