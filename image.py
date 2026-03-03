import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def readImage():
    imgPath = os.path.join("data", 'cat.jpg')       #path to the image
    img = cv.imread(imgPath)        # read the image
    cv.imshow('Cat', img)           # display the image in a window
    cv.waitKey(0)                   # wait for a key press to close the window  

def writeImage():
    imgPath = os.path.join("data", 'cat.jpg')       #path to the image
    img = cv.imread(imgPath)        # read the image
    outPath = os.path.join("data\outputs", 'cat.jpg')       #path to save the image
    cv.imwrite(outPath, img)       # save the image to the specified path

if __name__ == "__main__":
    #readImage()
    writeImage()

    