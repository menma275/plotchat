import cv2

def capture():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print('Camera open failed')
        exit()

    ret, frame = cap.read()

    if ret:
        cv2.imwrite('capture.jpg', frame)
        print('capture saved')

    cap.release()

    return frame

capture()
