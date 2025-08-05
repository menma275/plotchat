import cv2
import numpy as np
import requests


def capture():
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Camera open failed")
        exit()

    ret, frame = cap.read()

    cap.release()

    return frame


def captureESP32():
    url = "http://192.168.10.10/capture"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to get image from ESP32-CAM")
        return None

    # JPEG バイナリを NumPy 配列に変換して OpenCV 画像としてデコード
    img_array = np.frombuffer(response.content, dtype=np.uint8)
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    return frame


# capture()
