# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:03:16 2020

@author: NISHANT
"""
#Feature Detection and Description.
"""
For understanding  this we recall jisaw puzzle game where we combine multiple 
small pieces in correct order by identifying its corners , shape and pattern.

On the basis of all these we all detect corners in images with so many approaches,
"""

#Harris Corner Detection 

"""
OpenCV has the function cv2.cornerHarris() for this purpose. Its arguments are :

img - Input image, it should be grayscale and float32 type.
blockSize - It is the size of neighbourhood considered for corner detection
ksize - Aperture parameter of Sobel derivative used.
k - Harris detector free parameter in the equation.
"""
import numpy as np
import cv2 as cv

img = cv.imread('Data\\shapes.png')

cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)

res= cv.cornerHarris(gray, 2, 3, 0.04)

res = cv.dilate(res, None)

img[res > 0.01 * res.max()] = [0, 0, 255]  # marked color

cv.imshow('dst', img)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()



#-------------------------------------------


#We will learn about the another corner detector: Shi-Tomasi Corner Detector
#We will see the function: cv2.goodFeaturesToTrack().
#Shi- Tomasi approach is more effective as compared with Harris Corner detection

#In this we limit the number of corners and corners quality.
#It is more user friendly.

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Data\\shapes.png')
#image must be in gary
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#parameters (img,no.of corner,quality_level,min_distance between corner)
corners = cv2.goodFeaturesToTrack(gray,10,0.01,20)
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow("res==",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
