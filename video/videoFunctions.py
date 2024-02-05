# video_utils.py
import numpy as np
import cv2 as cv

def setup_camera(video_source):
    cap = cv.VideoCapture(video_source)
    
    if not cap.isOpened():
        print("Error opening the video file")
        return None
    
    if video_source == 0:
        cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, 360)
    
    return cap

