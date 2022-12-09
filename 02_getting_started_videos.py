import cv2
import numpy as np

cap = cv2.VideoCapture('./data/slow_traffic_small.mp4')
# cap = cv2.VideoCapture(0)  # file or 'number' for cameras

fourcc = cv2.VideoWriter_fourcc(*'XVID')

# name , ___, frames per seconds, size
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        out.write(frame)  # save video
        # print(cap.get(cv2. CAP_PROP_FRAME_WIDTH))
        # print(cap.get(cv2. CAP_PROP_FRAME_HEIGHT))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # grayscale video
        cv2.imshow('frame', np.flip(frame, 1))  # flip to mirror video

        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
