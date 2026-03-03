import numpy as np
import cv2 as cv
import os

def readVideo():
    cap = cv.VideoCapture(0)     # capture video from the default camera (0)

    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    while True:
        ret, frame = cap.read()   # read a frame from the video

        if not ret:
            print("Error: Could not read frame.")
            break

        cv.imshow('Video', frame)  # display the frame in a window

        if cv.waitKey(1) & 0xFF == ord('q'):  # wait for 'q' key to exit
            break

    cap.release()              # release the video capture object
    cv.destroyAllWindows()     # close all OpenCV windows

def readVideoFile():
    videoPath = os.path.join("data", 'video.mp4')  # path to the video file
    cap = cv.VideoCapture(videoPath)  # capture video from the specified file

    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    while True:
        ret, frame = cap.read()   # read a frame from the video

        if not ret:
            print("End of video reached.")
            break

        cv.imshow('Video', frame)  # display the frame in a window

        if cv.waitKey(25) & 0xFF == ord('q'):  # wait for 'q' key to exit
            break

    cap.release()              # release the video capture object
    cv.destroyAllWindows()     # close all OpenCV windows

if __name__ == "__main__":
    #readVideo()
    readVideoFile()