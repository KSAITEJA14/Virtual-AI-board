import os
from math import sqrt

def detectAction(hand_landmarks, image_shape):
    """
    Detects the user's action (Erasing, Drawing, or Unknown) based on hand landmarks and image shape.
    """
    if isErasing(hand_landmarks, image_shape):
        return "Erase"
    if isDrawing(hand_landmarks, image_shape):
        return "Draw"
    return "unknown"

def calcDistance(p1, p2):
    """
    Calculates the Euclidean distance between two points.
    """
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def isErasing(hand_landmarks, image_shape):
    """
    Checks if the erasing conditions are met.
    """
    h, w = image_shape
    index_tip = (hand_landmarks.landmark[8].x * w, hand_landmarks.landmark[8].y * h)
    middle_tip = (hand_landmarks.landmark[12].x * w, hand_landmarks.landmark[12].y * h)
    index_mcp = (hand_landmarks.landmark[5].x * w, hand_landmarks.landmark[5].y * h)
    
    return calcDistance(index_tip, middle_tip) < calcDistance(index_tip, index_mcp) // 3

def isDrawing(hand_landmarks, image_shape):
    """
    Checks if the drawing conditions are met.
    """
    w = image_shape[1]
    thumb_tip_x = hand_landmarks.landmark[4].x * w
    index_mcp_x = hand_landmarks.landmark[2].x * w

    return thumb_tip_x > index_mcp_x

def checkColor(hand_landmarks, image_shape, color_change, color_num):
    """
    Checks for a change in pen color.
    """
    h, w = image_shape
    index_tip_y = hand_landmarks.landmark[8].y * h
    index_mcp_y = hand_landmarks.landmark[5].y * h
    wrist_y = hand_landmarks.landmark[0].y * h

    curr_result = wrist_y > index_tip_y > index_mcp_y
    return (color_num + 1, True) if curr_result != color_change else (color_num, False)