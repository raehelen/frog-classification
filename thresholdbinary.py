import cv2
import numpy as np

def doThreshold(img):

    #retval, threshold = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

    #grayscale the image
    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #threshold the image
    retval2, threshold2 = cv2.threshold(grayscaled, 120, 255, cv2.THRESH_BINARY)

    #cv2.imwrite('thresholdcolour.jpg', threshold)
    #cv2.imwrite('./frog_templates/thresholdfrog2.jpg', threshold2)
    

    return threshold2
