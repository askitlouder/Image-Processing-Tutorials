#Adaptive thresholding -
#We use it beacuse simple thresholding not able to handle 
#different type of low luminous pixels
# this, the algorithm calculate the threshold for a small regions of the image.
#so we get multiple threshold for diff. regions in same image.

#Adaptive Method - It decides how thresholding value is calculated.
#cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.


#threshold (img,pixel_thresh,_max_thresh_pixel,method,style,no._of_pixel,contact_mean)
import cv2 
import numpy as np

img = cv2.imread('Data\\page.jpg',0)
img = cv2.resize(img,(400,400))
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) #simple 
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) #adaptive
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2); #adaptive

cv2.imshow("Image", img)
cv2.imshow("THRESH_BINARY", th1)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
