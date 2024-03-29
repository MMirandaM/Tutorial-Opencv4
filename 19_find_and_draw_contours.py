import cv2
import numpy as np

img = cv2.imread('./data/opencvlogo.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


print(f'Number of contours: {len(contours)}')

cv2.drawContours(img, contours, -1, (0,255,0), 3)


cv2.imshow('image', img)
cv2.imshow('image gray', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()