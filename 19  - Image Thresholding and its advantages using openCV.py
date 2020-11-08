#Threholding is a segmentation techique which is use to separate selected object from an image.

#Image Thresholding -  If pixel value is greater than a threshold value
#it is assigned one value (may be white), 
#else it is assigned another value (may be black).
#thresholding is use to subtract image from background
#Thresholding is of  3 type -  Simple thresholding, Adaptive thresholding, Otsu’s thresholding
#image should be in gray scale
#simple thresholding(img,pixel_thresh,_max_thresh_pixel,style)
#it return 2 values - one is random data , second is threshold



import cv2 
import numpy as np

img = cv2.imread("Data\\black_white.png",0)
img = cv2.resize(img,(300,300))
cv2.imshow("data",img)

_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("1 - THRESH_BINARY",th1)
cv2.imshow("2 -THRESH_BINARY_INV ", th2)
cv2.imshow("3- THRESH_TRUNC", th3)
cv2.imshow("4 - THRESH_TOZERO", th4)
cv2.imshow("5 - THRESH_TOZERO_INV", th5)
cv2.waitKey(0)
cv2.destroyAllWindows()
