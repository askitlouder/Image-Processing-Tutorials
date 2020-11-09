# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 19:07:37 2020

@author: NISHANT
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 18:09:39 2020

@author: NISHANT
"""


#Cat face detection using har cascade
import cv2
import numpy
face=cv2.CascadeClassifier("Data\\cascades\\haarcascade_frontalcatface.xml") #for detecting face

image=cv2.imread("Data\\dogcat2.jpg")
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #convert into gray so color not effect accuracy

#parameters(img,scale_factor[reduce image size],min_neighbour)
faces = face.detectMultiScale(gray,1.1,1)   #for  faces

for(x,y,w,h) in faces:
    
    image=cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,205),3)
    
    
    
image = cv2.resize(image,(800,700))
cv2.imshow("Face Detected",image)
cv2.waitKey(0)
cv2.destroyAllWindows()    
