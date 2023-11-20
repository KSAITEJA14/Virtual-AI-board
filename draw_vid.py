import cv2
import time
import mediapipe as mp 
import numpy as np
from detectActions import detectAction, checkColor

# def mediapipe_results(frame_infos):
def mediapipe_results(frame,circles,color_change,color_num,pen_color,pen_size,mpHands,hands,mp_draw):

    flip = True 
    eraser_size = 100
   
    ## Stores previously drawing circles to give continous lines
    pen_color_changes = {0:"(255,0,0)",1:"(0,255,0)",2:"(0,0,255)",3:"(0,0,0)"}

    if flip : 
        frame = cv2.flip(frame,1)
        
    h,w,c = frame.shape

    h = h*2
    w = w*2
    frame = cv2.resize(frame,(w,h))

    # frame = np.zeros([h,w,c],dtype=np.uint8)
    # frame.fill(255)

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #processes the keypoints of the hand
    results = hands.process(img_rgb)

    if not results.multi_hand_landmarks : 
        pass
    else : 
        for hand_landmarks in results.multi_hand_landmarks :
            mp_draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

            # detects the type of action done 
            action = detectAction(hand_landmarks,(h,w))

            color_num, color_change = checkColor(hand_landmarks,(h,w),color_change,color_num)
            
            if color_change:
                pen_color = eval(pen_color_changes[color_num%4])
            
            ## Draw mode
            if action == 'Draw': 
                index_x = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].x
                index_y = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y
                pos = [(int(index_x*w), int(index_y*h)),eval(pen_color_changes[color_num%4])]
               
                cv2.circle(frame, pos[0], 20, (0,0,0), 2)
                circles.append(pos)

            ## Erase mode
            elif action == 'Erase':
                eraser_mid = [
                        int(hand_landmarks.landmark[8].x * w),
                        int(hand_landmarks.landmark[8].y * h)
                    ]
               
                bottom_right = (eraser_mid[0]+eraser_size, eraser_mid[1]+eraser_size)
                top_left = (eraser_mid[0]-eraser_size, eraser_mid[1]-eraser_size)

                cv2.rectangle(frame, top_left, bottom_right, (0,0,255), 5)
                
                try : 
                    for pt in range(len(circles)):
                        if circles[pt][0][0]>top_left[0] and circles[pt][0][0]<bottom_right[0]: 
                            if circles[pt][0][1]>top_left[1] and circles[pt][0][1]<bottom_right[1]:
                                circles.pop(pt)
                except IndexError : 
                    pass
            
            elif action == "pause": 
                
                index_x = hand_landmarks.landmark[8].x
                index_y = hand_landmarks.landmark[8].y
                pos = (int(index_x*w), int(index_y*h))

                cv2.circle(frame, pos, 20, (0,0,255), 2)

    return frame, circles, pen_size, pen_color, color_change, color_num