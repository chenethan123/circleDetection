# main.py
import cv2 as cv
#Imports from seperate files
from videoFunctions import setup_camera, detect_circles

#Calls the necessary functions
def main(video_source):
    cap = setup_camera(video_source)
    
    if cap is None:
        return

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
    #Video path bc VSC is picky
    videoPath = r"C:\Users\Ethan\Desktop\newWork\circleDetection\soda.mov"
    videoSource = videoPath #Normally you would just do "soda.mov" but it woudnt work for me 
    colorImage = True

    main(videoSource)
