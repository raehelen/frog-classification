## Find object by orb features matching

import numpy as np
import cv2

def doHomography(target, template):

    #imgname = "frog10.jpg"          # query image (small object)
    #imgname2 = "frog10.jpg"         # train image (large scene)

    MIN_MATCH_COUNT = 4

    ## Create ORB object and BF object(using HAMMING)
    orb = cv2.ORB_create()
    img1 = cv2.imread(target)
    img2 = cv2.imread(template)

    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    ## Find the keypoints and descriptors with ORB
    kpts1, descs1 = orb.detectAndCompute(gray1,None)
    kpts2, descs2 = orb.detectAndCompute(gray2,None)

    ## match descriptors and sort them in the order of their distance
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descs1, descs2)
    dmatches = sorted(matches, key = lambda x:x.distance)

    ## extract the matched keypoints
    src_pts  = np.float32([kpts1[m.queryIdx].pt for m in dmatches]).reshape(-1,1,2)
    dst_pts  = np.float32([kpts2[m.trainIdx].pt for m in dmatches]).reshape(-1,1,2)

    
    # store all the good matches as per Lowe's ratio test.
    good = []
    for m,n in matches:
        if m.distance < loweDistance * n.distance: # used to be 0.7
            good.append(m)

    # if there are enough "good matches"
    return len(good)
        

        
    ## draw found regions
    #img2 = cv2.polylines(img2, [np.int32(dst)], True, (0,0,255), 1, cv2.LINE_AA)
    #cv2.imwrite("out.jpg", img2)

    ## draw match lines
    #res = cv2.drawMatches(img1, kpts1, img2, kpts2, dmatches[:20],None,flags=2)

    #cv2.imwrite("out2.jpg", res);
