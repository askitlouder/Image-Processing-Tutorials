#How to read Video from any folder using opencv

import cv2

#Here with the help of videoCapture fucntion we easily ready any video.
"""
cap = cv2.VideoCapture("Data\\Pirates.mp4")   #Here parameter is a path of any video

while True:
    ret, frame = cap.read()   #here read the frame
    #get height and width of frame
    print("Width ==>",cv2.CAP_PROP_FRAME_WIDTH)
    print("Height==>",cv2.CAP_PROP_FRAME_HEIGHT)
    
    frame = cv2.resize(frame,(700,450))
    gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame,-1) 
    cv2.imshow('Colorframe',frame)
    cv2.imshow("Gray Frame",gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):   #press to exit
        break
   
# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
"""

#Capture  video from webcam and save it

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   #Here parameter 0 is a path of any video use for webcam
print("check===",cap.isOpened())

#it is 4 byte code which is use to specify the video codec
#Various codec -- 
#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame
    
    if ret==True:
        
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #here flip is used to lip the video at recording time
        frame = cv2.flip(frame,0)
        output.write(gray)
        
        cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
    else:
        break
 
# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()







