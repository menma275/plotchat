import cv2

def capture():
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print('Camera open failed')
        exit()

    ret, frame = cap.read()

    cap.release()

    return frame

# capture()
