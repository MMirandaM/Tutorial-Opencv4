import cv2
import numpy as np

img = cv2.imread('messi5.jpg', 1)
img2 = cv2.imread('opencv-logo.png', 1)
img3 = np.ones([5,5,3], dtype=np.uint8)

print(img.shape)  # rows, columns, channelsg
print(img.size)  # numbers of pixel
print(img.dtype)
print(img3.dtype)

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# ball = img[260:340, 330:390]
# img[253:333, 100:160] = ball

# img[273:333, 160:220] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
img3 = cv2.resize(img3, (512, 512))

black = img3[260:340, 330:390]
img[253:333, 100:160] = black

# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .2, img2, .4, 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

