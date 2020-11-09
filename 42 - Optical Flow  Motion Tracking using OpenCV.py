# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 18:00:17 2020

@author: NISHANT
"""
#Optical Flow-- Lucas-Kanade method
#Optical flow is the pattern of apparent motion of image objects
#between two consecutive frames caused by the movemement 
#of object or camera.

#Optical flow works on several assumptions:

#The pixel intensities of an object do not change b/w consecutive frames.
#Neighbouring pixels have similar motion.


"""
To decide the points, we use cv2.goodFeaturesToTrack(). 
We take the first frame, detect some Shi-Tomasi corner points in it, 
then we iteratively track those points 
using Lucas-Kanade optical flow. For the function
cv2.calcOpticalFlowPyrLK() we pass the previous frame, 
previous points and next frame. It returns next points 
along with some status numbers which has a value of 1 if next 
point is found, else zero. We iteratively pass these next points 
as previous points in next step.

"""





import cv2
import numpy as np

cap = cv2.VideoCapture("Data\\test2.mp4")

# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(100,3))

# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while(1):
    ret,frame = cap.read()
#    resize = cv2.resize(frame, (640, 480))
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray,
                                           frame_gray, p0, 
                                           None, **lk_params)

    # Select good points
    good_new = p1[st==1]
    good_old = p0[st==1]

    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
    
    img = cv2.add(frame,mask)
    img = cv2.resize(img,(700,600))
    cv2.imshow('frame',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)

cv2.destroyAllWindows()
cap.release()


#Gunner Farneback’s algorithm




import cv2
import numpy as np
cap = cv2.VideoCapture("H:\\Data\\test2.mp4")

ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255

while(1):
    ret, frame2 = cap.read()
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 
                                        0.5, 3, 15, 3, 5, 1.2, 0)

    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    im1 = cv2.add(frame2,rgb)
    im1 = cv2.resize(im1,(700,430))
    cv2.imshow('frame2',im1)
    k = cv2.waitKey(60) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('opticalfb.png',frame2)
        cv2.imwrite('opticalhsv.png',rgb)
    prvs = next

cap.release()
cv2.destroyAllWindows()



















