import cv2

img = cv2.imread('./data/lena.jpg', 1)  # 1 - color img, 0 - grayscale img
# -1 - alpha channel

print(img)
if img is not None:
    cv2.imshow('Lena', img)
    key_press = cv2.waitKey(0)  # milisseconds to wait a screen
    # 0 - wait a key
    if key_press == 27:
        cv2.destroyAllWindows()
    elif key_press == ord('s'):
        cv2.imwrite('lena_copy.png', img)
else:
    print('Img not found')
