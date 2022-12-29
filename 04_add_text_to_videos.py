import cv2
from datetime import datetime as dt

cap = cv2.VideoCapture(0)

# resolution
cap.set(3, 720)  # width
cap.set(4, 720)  # height

# cat.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
# cat.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width:' + str(cap.get(3))
        datet = str(dt.now())
        frame = cv2.putText(frame, datet, (10, 80), font,
                            1, (0, 255, 255), 5, cv2.LINE_4)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
