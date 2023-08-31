import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic


import tensorflow as tf
from draw_vid import mediapipe_results


def set_gpu_memory_growth():
    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    if physical_devices:
        try:
            print("---------------------GPU available")
            for dev in physical_devices:
                tf.config.experimental.set_memory_growth(dev, True)
        except RuntimeError as e:
            print(e)
    else:
        print("--------------Using CPU device")

# set cpu or gpu
set_gpu_memory_growth()

cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as holistic:
    i = 0

    circles = []
    color_change, color_num = False, 0
    pen_color = 0
    pen_size = 15
    min_conf = 0.5
    max_hands = 2

    mpHands = mp.solutions.hands
    hands = mpHands.Hands(
      static_image_mode=False,
      max_num_hands=max_hands,
      min_detection_confidence=min_conf,
      min_tracking_confidence=min_conf
    )
    mp_draw = mp.solutions.drawing_utils

    with mpHands.Hands(
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5) as hands:

      while True:
        success, frame = cap.read()  # read the camera frame
        if not success:
          break
        else:

            frame, circles, pen_size, pen_color, color_change, color_num = mediapipe_results(frame, circles, color_change, color_num,
                                                                                    pen_color, pen_size, mpHands, hands,
                                                                                    mp_draw)

            for position in range(len(circles)):
                pen_color = circles[position][1]
                frame = cv2.circle(frame, circles[position][0], pen_size, pen_color, -2)

            cv2.imshow('MediaPipe Holistic', frame)
            
            if cv2.waitKey(5) & 0xFF == 27:
                break
            
    # Flip the image horizontally for a selfie-view display.
    # cv2.imwrite(f"images/{i}.png",image)
    
cap.release()