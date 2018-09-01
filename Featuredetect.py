## Find object by orb features matching

import numpy as np
import cv2

def doHomography(img1, img2):

    #imgname = "frog10.jpg"          # target image (small object)
    #imgname2 = "frog10.jpg"         # template image (large scene)

    MIN_MATCH_COUNT = 4

    ## Create ORB object and BF object(using HAMMING)
    orb = cv2.ORB_create()
    #img1 = cv2.imread(img1, 0)
    #img2 = cv2.imread(img2, 0)

    #gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    #gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    ## Find the keypoints and descriptors with ORB
    kpts1, descs1 = orb.detectAndCompute(img1,None)
    kpts2, descs2 = orb.detectAndCompute(img2,None)

    ## match descriptors and sort them in the order of their distance
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descs1, descs2)
    dmatches = sorted(matches, key = lambda x:x.distance)

    ## extract the matched keypoints
    src_pts  = np.float32([kpts1[m.queryIdx].pt for m in dmatches]).reshape(-1,1,2)
    dst_pts  = np.float32([kpts2[m.trainIdx].pt for m in dmatches]).reshape(-1,1,2)

    
    # store all the good matches as per Lowe's ratio test.
    good = []
    for m in matches:
        if m.distance < 0.7:
            good.append(m)

    # if there are enough "good matches"
    return len(good)
        
       
 
    ## draw match lines
    #res = cv2.drawMatches(img1, kpts1, img2, kpts2, dmatches[:20],None,flags=2)
    #cv2.imwrite('C:\Python27\jonny\homography.jpg', res);
