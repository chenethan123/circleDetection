# main.py
import cv2 as cv
from videoFunctions import setup_camera
import numpy as np

def detect_circles(frame, cap, color_image=False):
    # Convert the frame to grayscale
    gframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Hough Circles to detect
    circles = cv.HoughCircles(gframe, cv.HOUGH_GRADIENT, 1, int(cap.get(cv.CAP_PROP_FRAME_WIDTH)) * 2, param1=40, param2=40, minRadius=325, maxRadius=400)

    # Choose the frame to display based on the color_image flag
    if color_image:
        displayed_frame = frame
    else:
        displayed_frame = gframe

    try:
        # If circles are detected, draw them
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv.circle(displayed_frame, (i[0], i[1]), i[2], (0, 255, 0), 5)
            cv.circle(displayed_frame, (i[0], i[1]), 2, (0, 0, 255), 5)
    except TypeError:
        pass
    
    return displayed_frame

def main(video_source):
    # Set up the camera
    cap = setup_camera(video_source)
    
    # is the cam successful?
    if cap is None:
        return
    
    # Create a window for displaying the detected circles
    cv.namedWindow('detected circles', cv.WINDOW_NORMAL)
    cv.resizeWindow('detected circles', 500, 700)
    
    # process frames
    while cap.isOpened():
        ret, frame = cap.read()

        # checks if frame is read
        if ret:
            # Detect circles in the frame and display the result
            displayed_frame = detect_circles(frame, cap, color_image=colorImage)
            cv.imshow('detected circles', displayed_frame)
            
            # End when q pressed
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

    # Release the camera and close the display window
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    # Specify the path to the video file, changes depending on machine
    videoPath = r"C:\Users\Ethan\Downloads\IMG_0866.MOV"
    videoSource = videoPath
    
    # Set the colorImage flag to True for displaying color images, false would display a gray image
    colorImage = True

    # Run the main function 
    main(videoSource)
