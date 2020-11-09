# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 18:09:39 2020

@author: NISHANT
"""


#Face Detection using haarcascade file 
import cv2
import numpy
face=cv2.CascadeClassifier("Data\\cascades\\haarcascade_frontalface_default.xml") #for detecting face
eye = cv2.CascadeClassifier('Data\\cascades\\haarcascade_eye.xml') #for detecting eyes

image=cv2.imread("Data\\a.jpg")
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #convert into gray 

#parameters(img,scale_factor[reduce image size],min_neighbour)
faces = face.detectMultiScale(gray,4,4)   #for  faces

for(x,y,w,h) in faces:
    
    image=cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,205),3)
    
    #Now detect eyes
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye.detectMultiScale(roi_gray,1.2,1)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    
image = cv2.resize(image,(800,700))
cv2.imshow("Face Detected",image)
cv2.waitKey(0)
cv2.destroyAllWindows()    
