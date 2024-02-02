# video_utils.py
import numpy as np
import cv2 as cv

def setup_camera(video_source):
    #Opens the video
    cap = cv.VideoCapture(video_source)
    #If the video is not opened, it prints an error
    if not cap.isOpened():
        print("Error opening the video file")
        return None
    #Sets the video parameters
    if video_source == 0:
        cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, 360)
    
    return cap

def detect_circles(frame, cap, color_image=False):
    #Gray scale
    gframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #Paramaters for detecting circles
    circles = cv.HoughCircles(gframe, cv.HOUGH_GRADIENT, 1, int(cap.get(cv.CAP_PROP_FRAME_WIDTH)) * 2, param1=100, param2=50, minRadius=70, maxRadius=0)

    if color_image:
        displayed_frame = frame
    else:
        displayed_frame = gframe

    try:
        #Used to display the circle
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv.circle(displayed_frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv.circle(displayed_frame, (i[0], i[1]), 2, (0, 0, 255), 3)
    except TypeError:
        pass
    
    return displayed_frame

