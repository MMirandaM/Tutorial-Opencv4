import cv2
import numpy as np

# img = cv2.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0, 0), (400, 400), (147, 96, 44), 20)
img = cv2.arrowedLine(img, (0, 255), (400, 400), (255, 96, 255), 20)

img = cv2.rectangle(img, (0, 0), (400, 400), (147, 96, 44),
                    100)  # -1 fill all retangle

img = cv2.circle(img, (477, 63), 63, (0, 255, 0), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10, 500), font, 4,
                  (0, 255, 255), 10, cv2.LINE_8, False)


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
