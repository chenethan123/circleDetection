# main.py
import cv2 as cv
from videoFunctions import setup_camera
import numpy as np

def detect_circles(frame, cap, color_image=False):
    gframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    circles = cv.HoughCircles(gframe, cv.HOUGH_GRADIENT, 1, int(cap.get(cv.CAP_PROP_FRAME_WIDTH)) * 2, param1=40, param2=40, minRadius=325, maxRadius=400)

    if color_image:
        displayed_frame = frame
    else:
        displayed_frame = gframe

    try:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv.circle(displayed_frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv.circle(displayed_frame, (i[0], i[1]), 2, (0, 0, 255), 3)
    except TypeError:
        pass
    
    return displayed_frame

def main(video_source):
    cap = setup_camera(video_source)
    
    if cap is None:
        return
    cv.namedWindow('detected circles', cv.WINDOW_NORMAL)
    cv.resizeWindow('detected circles', 500, 700)
    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            displayed_frame = detect_circles(frame, cap, color_image=colorImage)

            cv.imshow('detected circles', displayed_frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    videoPath = r"C:\Users\Ethan\Downloads\IMG_0866.MOV"
    videoSource = videoPath
    colorImage = True

    main(videoSource)
