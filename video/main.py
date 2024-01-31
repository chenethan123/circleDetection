import cv2
import numpy as np

# Open a video file or use a camera (0 for default camera).
video_capture = cv2.VideoCapture('your_video.mp4')  
while True:
    # Read a frame from the video.
    ret, frame = video_capture.read()
    
    # Break the loop if the video has ended.
    if not ret:
        break

    # Convert the frame to grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur using a 3 * 3 kernel.
    gray_blurred = cv2.blur(gray, (1, 1))

    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(gray_blurred,
				cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
			param2 = 30, minRadius = 300, maxRadius = 0)


    # Draw circles that are detected.
    if detected_circles is not None:
        # Convert the circle parameters a, b, and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]

            # Draw the circumference of the circle.
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2)

            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 2)

        # Display the frame with detected circles.
        cv2.imshow("Detected Circles", frame)

    # Break the loop if 'q' key is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows.
video_capture.release()
cv2.destroyAllWindows()
