# video_utils.py
import numpy as np
import cv2 as cv

def setup_camera(video_source):
    #Opens the cam
    cap = cv.VideoCapture(video_source)
    #Ccheck if cam is open
    if not cap.isOpened():
        print("Error opening the video file")
        return None
    #Sets a certain quality to reduce lag
    if video_source == 0:
        cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, 360)
    
    return cap

