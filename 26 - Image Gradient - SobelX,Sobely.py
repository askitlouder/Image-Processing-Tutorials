# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:26:50 2020

@author: NISHANT
"""
#Image Gradient--
#It is a directional change in the color or intensity in an image.
#It is most important part to find inormation from image
#Like finding edges within the images.
#There are various methods to find image gradient.
#These are - Laplacian Derivatives,SobelX and SobelY.
#All these functions have diff. mathematical approach to get result.
#All load image in the gray scale

#Don't Worry about Mathematics behind all these function
#we just use these to get our work in easy manner.
  
import cv2
import numpy as np


#load image into gray scale
img = cv2.imread("Data\\page.jpg")
img = cv2.resize(img,(400,300))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Laplacian Derivative---It calculate laplace derivate
#parameter(img,data_type for -ve val,ksize)
#kernal size must be odd
lap = cv2.Laplacian(img_gray,cv2.CV_64F,ksize = 3) #also pass kernal size
lap = np.uint8(np.absolute(lap))

#Sobel operation - 
# is a joint Gausssian smoothing plus differentiation operation, 
#so it is more  resistant to noise
#This is use for x and y bth
#parameter (img,type for -ve val,x = 1,y = 0,ksize)
#Sobel X focus on vertical lines
#Sobel y focus on horizontal lines

sobelX = cv2.Sobel(img_gray,cv2.CV_64F,1,0,ksize = 3) #here 1 means x direction
sobelY = cv2.Sobel(img_gray,cv2.CV_64F,0,1,ksize = 3) #here 1 means y direction

sobelX = np.uint8(np.absolute(sobelX))
sobelY= np.uint8(np.absolute(sobelY))

#finally combine sobelX and sobelY togather
sobelcombine = cv2.bitwise_or(sobelX,sobelY)

cv2.imshow("original==",img)
cv2.imshow("gray====",img_gray)
cv2.imshow("Laplacian==",lap)
cv2.imshow("SobelX===",sobelX)
cv2.imshow("SobelY==",sobelY)
cv2.imshow("COmbined image==",sobelcombine)



#Now plot all the images on graph
titles = ["original","gray","laplacian","sobelX","sobelY","combined"]
images = [img,img_gray,lap,sobelX,sobelY,sobelcombine]

#if you want then plot it
from matplotlib import pyplot as plt
for i in range(6):
    plt.subplot(3,2, i+1), 
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

cv2.waitKey(0)
cv2.destroyAllWindows()
