# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 19:43:18 2020

@author: NISHANT
"""
#GrabCut Algoritm with the help of this algoritm we easily
#cutoff any foreground object from image or video.
#It works like a rectangle portion mark on the image
#and area outise the rectangle is treat as a extra part
#so this algo remove it completely.
#Gaussian mixtuere model help to achieve the target



import	numpy  as  np
import	cv2

img  =	cv2.imread('Data\\car.jpg')
img = cv2.resize(img,(800,800))
mask =	np.zeros(img.shape[:2],np.uint8)
 
 
bgdModel =  np.zeros((1,65),np.float64)*255
fgdModel =  np.zeros((1,65),np.float64)*255
 
#parameter(img,mask,rect,bgmodel,fgmodel,iter,method) 
rect =	(134,150,660,730)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,
            cv2.GC_INIT_WITH_RECT)
 
 
mask2  =  np.where((mask==2)|(mask==0),0,1).astype('uint8')
img  =	img*mask2[:,:,np.newaxis]
 
cv2.imshow("res==",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
