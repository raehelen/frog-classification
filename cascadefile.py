#import the necessary packages
import cv2

def doCascade(image):

    # load the input image and convert it to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # load the detector Haar cascade, then detect the frog in the input image
    detector = cv2.CascadeClassifier("180x120/cascade.xml")
    rects = detector.detectMultiScale(gray) #, scaleFactor=1.3, minNeighbors=10, minSize=(75, 75))
    
    # Draw only the largest rectangle
    (x, y, w, h) = sorted(rects, key=lambda x: x[2]*x[3], reverse=True)[0]
    #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #cv2.putText(image, "Frog", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

    # show the detected frogs
    #cv2.imwrite("out/", image)

    return image[y:y+h, x:x+w]
