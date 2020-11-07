#Create your own color picker -

import cv2
import numpy as np

def cross(x):
    pass
#create a black imgae
img = np.zeros((300,512,3),np.uint8) #empty image
cv2.namedWindow("Color Picker")

#Creating switch for on and of the trackbars
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'Color Picker',0,1,cross)

#Creating TrackBars For Adjusting Colors
cv2.createTrackbar("R","Color Picker",0,255,cross)
cv2.createTrackbar("G","Color Picker",0,255,cross)
cv2.createTrackbar("B","Color Picker",0,255,cross)

#Now creating logic to handle trackbars
while True:
    cv2.imshow("Color Picker",img)
    k = cv2.waitKey(1) & 0xFF
    if k==27: #for exit
        break
    
    #set current positions of four bars
    s = cv2.getTrackbarPos(switch,"Color Picker") #switch
    r = cv2.getTrackbarPos("R","Color Picker")
    g = cv2.getTrackbarPos("G","Color Picker")
    b = cv2.getTrackbarPos("B","Color Picker")
    
    if s==0:
        img[:] = 0
    else:
        img[:] = [r,g,b] #here openCV support BGR
cv2.destroyAllWindows()
    













    
