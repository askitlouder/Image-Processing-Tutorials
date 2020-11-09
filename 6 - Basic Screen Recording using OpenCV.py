#Screen Recorder ---
"""
import pyautogui as p
import cv2 as c
import numpy as np

#Create resolution
rs = p.size()

#filename in which we store recording
fn = input("Please Enter any file name and Path")
#Fix the frame rate
fps = 60.0
fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn,fourcc,fps,rs)

#create recording module
c.namedWindow("LIve_Recording",c.WINDOW_NORMAL)

#Resize the window
c.resizeWindow("Live",(600,400))

while True:
    img = p.screenshot() #image
    f = np.array(img) #convert image into array
    f = c.cvtColor(f,c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow("screenshot", f)
    if c.waitKey(1) == ord("q"):
        break

c.destroyAllWindows()
output.release()  
"""

#Capture Multiple Images and Store in a folder

import cv2

vidcap = cv2.VideoCapture(0)
ret,image = vidcap.read()#READ THE VIDEO



count = 0

while True:
  if ret == True:
      cv2.imwrite("frames\\imgN%d.jpg" % count, image)     # save frame as JPEG file
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100)) #used to hold speed of frane generation
      ret,image = vidcap.read()
      cv2.imshow("res",image)
      print ('Read a new frame:',count ,ret)
      count += 1
      if cv2.waitKey(1) & 0xFF == ord("q"):
          break
          cv2.destroyAllWindows()
  else:
      break

vidcap.release() 
cv2.destroyAllWindows()  











