# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 17:34:13 2020

@author: NISHANT
"""
#Object Tracking using Meanshift Algo.
#The idea behind this algo is to move small window to get the high 
#density pixels same as histogram backprojection.

#Steps to use this algo-----
#First setup target and find its histogram for backproject the traget.
#ALso set one initial location
#setup the termination criteria

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('Data\\test2.mp4')

# take first frame of the video
ret, frame = cap.read()

# setup initial location of window
x, y, width, height = 580, 30, 80,150
track = (x, y ,width, height)

# set up the ROI for tracking
roi = frame[y:y+height, x : x+width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)),
np.array((180., 255., 255)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255,cv.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
termntn = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
cv.imshow('roi',roi)
while  True:
    ret, frame = cap.read()
    
    if ret == True:

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        
        # apply meanshift to get the new location
        ret, track = cv.meanShift(dst, track, termntn)
        
        # Draw it on image
        x,y,w,h = track
        final = cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)

        cv.imshow('dst', dst)
        frame = cv.resize(final,(600,600))
        cv.imshow('final_image',frame)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break
cv.destroyAllWindows()

#There are few disadvantages of this algo
#Fixe of target window should not be changed.
#to manuaaly pass roi and then detect our target




#CAMshift (Continuously Adaptive Meanshift)


import numpy as np
import cv2 as cv
cap = cv.VideoCapture('H:\\Data\\test2.mp4')

# take first frame of the video
ret, frame = cap.read()

# setup initial location of window
x, y, width, height = 580, 30, 80,150
track = (x, y ,width, height)

# set up the ROI for tracking
roi = frame[y:y+height, x : x+width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255,cv.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
termntn = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
cv.imshow('roi',roi)
while  True:
    ret, frame = cap.read()
    
    if ret == True:

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        
        # apply meanshift to get the new location
        ret, track = cv.CamShift(dst, track, termntn)
        
        # Draw it on image
        #x,y,w,h = track
        #final = cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)
        
        #Try to draw rotating rectangle
        pts =cv.boxPoints(ret)
        pts = np.int64(pts)
        final = cv.polylines(frame,[pts],True,(255,0,0),2)
        
        
        
        
        
        
        cv.imshow('dst', dst)
        frame = cv.resize(final,(600,600))
        cv.imshow('final_image',frame)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break
cv.destroyAllWindows()


















