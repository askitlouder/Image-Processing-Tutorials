#In this we try to perfrom roi extraction any shaped object

import cv2
import numpy as np

# Load two images
img1 = cv2.imread("Data\\hero1.jpg")
img2 = cv2.imread("Data\\strom_breaker.jpg")


img1 = cv2.resize(img1,(1024,650))
img2 = cv2.resize(img2,(600,650))

#I want to fix img2 data into img1
r,c,ch = img2.shape
#here first(y,x)
roi = img1[0:r,0:c]

#NOw creating mask for img1
img_gry = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#create mask using threshold
_, mask = cv2.threshold(img_gry, 50, 255, cv2.THRESH_BINARY)
#remove bg
mask_inv= cv2.bitwise_not(mask)

#put mask into roi
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of figure from original  image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
res = cv2.add(img1_bg,img2_fg)

final = img1

final[0:r,0:c]= res   #final output

cv2.imshow("Thor",img1)
cv2.imshow("Strom breaker",img2)
cv2.imshow(" Step -1 gry==",img_gry)
cv2.imshow("Step -2 Mask===",mask)
cv2.imshow("Step -3 Mask_inv",mask_inv)
cv2.imshow("Step -4 Mask_bg",img1_bg)
cv2.imshow("Step -5 Mask fg",img2_fg)
cv2.imshow("Step -6 -Res",res)
cv2.imshow("Step 7== FInal",final)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Remeber one thing the size of image which is your roi always smaller then 
#first image
"""
# Load two images
img1 = cv2.imread("H:\\Data\\hero1.jpg")
img2 = cv2.imread("H:\\Data\\hero2.jpg")
img1 = cv2.resize(img1,(1024,650))
img2 = cv2.resize(img2,(600,650))

#I want to fix img2 data into img1
r,c,ch = img2.shape
#here first(y,x)
roi = img1[:r,:c]

#NOw creating mask for img1
img_gry = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#create mask using threshold
_, mask = cv2.threshold(img_gry, 50, 255, cv2.THRESH_BINARY)
#remove bg
mask_inv= cv2.bitwise_not(mask)

#put mask into roi
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
res = cv2.add(img1_bg,img2_fg)

final = img1

final[0:r,0:c]= res   #final output

#cv2.imshow("Thor",img1)
#cv2.imshow("Ironman",img2)
cv2.imshow(" Step -1 gry==",img_gry)
cv2.imshow("Step -2 Mask===",mask)
cv2.imshow("Step -3 Mask_inv",mask_inv)
cv2.imshow("Step -4 Mask_bg",img1_bg)
cv2.imshow("Step -5 Mask fg",img2_fg)
cv2.imshow("Step -6 -Res",res)
cv2.imshow("Step 7== FInal",final)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

