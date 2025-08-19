import cv2
import numpy as np
import requests
import mediapipe as mp
import time


def capture():
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Camera open failed")
        exit()

    ret, frame = cap.read()

    cap.release()

    return frame


def captureESP32():
    url = "http://192.168.10.200/capture"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to get image from ESP32-CAM")
        return None

    # JPEG バイナリを NumPy 配列に変換して OpenCV 画像としてデコード
    img_array = np.frombuffer(response.content, dtype=np.uint8)
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    return frame


def captureWhenHandDisappears(capture_func=captureESP32, capture_delay=1.0):
    """Continuously capture frames from the ESP32-CAM until hand disappears."""
    mp_hands = mp.solutions.hands
    hands_module = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    )

    hand_present = False
    no_hand_start = None

    while True:
        frame = capture_func()
        if frame is None:
            continue

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands_module.process(rgb_frame)

        if result.multi_hand_landmarks:
            hand_present = True
            no_hand_start = None
        else:
            if hand_present:
                if no_hand_start is None:
                    no_hand_start = time.time()
                elif time.time() - no_hand_start > capture_delay:
                    print("Hand disappeared, capturing image...")
                    return frame


# capture()
