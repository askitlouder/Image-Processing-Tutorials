# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 16:35:31 2020

@author: NISHANT
"""
#Background Subtraction is a way to access the foreground objects.
#Technically, you need to extract the moving 
#foreground from static background.
#There are multiple approach for backgroud subtract

#We discuss all of them.

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('Data\\test2.mp4')


#old_algo = cv.bgsegm.createBackgroundSubtractorMOG()
algo1 = cv.createBackgroundSubtractorMOG2(detectShadows=True) #algo1 
algo2 = cv.createBackgroundSubtractorKNN(detectShadows=True)  #algo2
while True:
    ret, frame = cap.read()
    frame = cv.resize(frame,(600,400))
    if frame is None:
        break
    res1 = algo1.apply(frame)
    res2 = algo2.apply(frame)
    

    cv.imshow('original', frame)
    cv.imshow('res1',res1)
    cv.imshow('res2',res2)

    keyboard = cv.waitKey(60)
    if keyboard == 'q' or keyboard == 27:
        break
cap.release()
cv.destroyAllWindows()
