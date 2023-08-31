
import os 
from math import sqrt
    

def detectAction(hand_landmarks,image_shape):
    """
    Input: 
    hand_landmarks: information about the hand keypoints
    image_shape: shape of the image

    Description: 
    This function checks and concludes the state of the user (Erasing, drawing, pause)
    """ 
    
    if erase(hand_landmarks,image_shape):
        return "Erase"
    
    if isDrawing(hand_landmarks,image_shape):
        return "Draw"
    
    return "unknown"

def calc_distance(p1, p2):
    
    """
    Input: 
    p1 : [x1,y1]
    p2 = [x2,y2]

    Description: 
    This function calculates the distance betwen two points
    
    """
    
    # simple function, I hope you are more comfortable
    return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def erase(hand_landmarks,image_shape):
    """
    Input: 
    hand_landmarks: information about the hand keypoints
    image_shape: shape of the image

    Description: 
    This function checks the conditions for erasing  
    """
    h,w = image_shape
    index_finger_leftmost_x = (hand_landmarks.landmark[8].x)*w
    index_finger_leftmost_y = (hand_landmarks.landmark[8].y)*h

    middle_finger_tip_x = (hand_landmarks.landmark[12].x)*w
    middle_finger_tip_y = (hand_landmarks.landmark[12].y)*h

    index_finger_MCP_x = (hand_landmarks.landmark[5].x)*w
    index_finger_MCP_y = (hand_landmarks.landmark[5].y)*h

    pointA = (index_finger_leftmost_x, index_finger_leftmost_y) 
    pointB = (middle_finger_tip_x, middle_finger_tip_y) 
    pointC = (index_finger_MCP_x, index_finger_MCP_y) 
    
    distance1 = calc_distance(pointA, pointB) 
    distance2 = calc_distance(pointA, pointC) 
    return distance1 < distance2//3

def isDrawing(hand_landmarks,image_shape):
    """
    Input: 
    hand_landmarks: information about the hand keypoints
    image_shape: shape of the image

    Description: 
    This function checks the conditions for drawing 
    """

    _,w = image_shape

    thumb_tip_x = (hand_landmarks.landmark[4].x)*w
    index_finger_MCP_x = (hand_landmarks.landmark[2].x)*w

    return thumb_tip_x > index_finger_MCP_x

def checkColor(hand_landmarks,image_shape,color_change,color_num):
    
    '''
    Input: 
    hand_landmarks: information about the hand keypoints
    image_shape: shape of the image
    color_change: A default value (False) for color change
    color_num: a number denoting a specific color
    
    Description: 
    This function checks whether the user has changed the pen color. If they wish to, itll change
    the pen color.
    '''

    h,w = image_shape 
    curr_result = False

    index_finger_leftmost_y = (hand_landmarks.landmark[8].y)*h
    index_finger_MCP_y = (hand_landmarks.landmark[5].y)*h
    wrist_y = (hand_landmarks.landmark[0].y)*h

    if wrist_y > index_finger_leftmost_y > index_finger_MCP_y:
        curr_result = True

    if color_change == curr_result:
        return color_num, False

    return color_num+1,True
