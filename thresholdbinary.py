import cv2
import numpy as np

def doThreshold(img):

    #retval, threshold = cv2.threshold(img, 76, 255, cv2.THRESH_BINARY)

    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    retval2, threshold2 = cv2.threshold(grayscaled, 76, 255, cv2.THRESH_BINARY)

    #cv2.imwrite('thresholdcolour.jpg', threshold)
    #cv2.imwrite('thresholdbinary.jpg', threshold2)

    return threshold2
