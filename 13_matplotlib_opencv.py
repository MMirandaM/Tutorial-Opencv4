import matplotlib.pyplot as plt
import cv2
import numpy as np


# img = cv2.imread('./data/lena.jpg', -1)
# cv2.imshow('./data/image', img)


# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.xticks([])
# plt.yticks([])
# plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()

img_g = cv2.imread('gradient.png', -1)

_, th1 = cv2.threshold(img_g, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img_g, 170, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img_g, 100, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img_g, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img_g, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original', 'Binary', 'Binary Inv', 'Trun', 'ToZero', 'ToZero Inv']
images = [img_g, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2,3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
