# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:01:34 2020

@author: NISHANT
"""
#Canny Edge Detection using OpenCV
#Canny Edge Detection is a popular edge detection approach.
#It is use  multi-stage algorithm to detect a edges.
#It was developed by John F. Canny in 1986.
#This approach combine with 5 steps.
# 1) -  NOise reduction(gauss)), 2) -Gradient calculation( ,
# 3) - Non-maximum suppresson, 4) - Double Threshold,
# 5) - Edge Tracking by Hysteresis 




import cv2
import numpy as np
"""
#load image into gray scale
img = cv2.imread("Data\\building.jpg")
img = cv2.resize(img,(600,700))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#canny(img,thresh1,thres2)thresh 1 and thresh2 at different lvl
canny = cv2.Canny(img_gray,20,150)

cv2.imshow("original==",img)
cv2.imshow("gray====",img_gray)
cv2.imshow("canny==",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""



#building trackbar with canny edge

#load image into gray scale
img = cv2.imread("Data\\building.jpg")
img = cv2.resize(img,(600,700))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def nothing(x):
    pass

cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold", "Canny", 0, 255, nothing)

while True:
    a= cv2.getTrackbarPos('Threshold','Canny')
    
    print(a)
    res = cv2.Canny(img_gray,a,255)
    cv2.imshow("Canny",res)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()






























