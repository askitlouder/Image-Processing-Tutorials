import cv2    #openCV use as cv2 in python

#Loads a color image. Any transparency of image will be neglected. It is the default flag.
#this function is used to read the image from location
img1 = cv2.imread('H:\\Data\\avengers.jpg',1)  
img1 = cv2.resize(img1,(1280,700))#width ,height
cv2.imshow("Colored Image",img1)  #It accept two parameters 1)- Name of screen ,2) -  Image
print("Give image with color==\n",img1)

#cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
img2 = cv2.imread('H:\\Data\\avengers.jpg',0)
img2 = cv2.resize(img2,(1280,700))#width ,height
cv2.imshow("Gray Scale Image",img2)
print("Image in gray scale==\n",img2)

#cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
img3 = cv2.imread('H:\\Data\\avengers.jpg',-1)
img3 = cv2.resize(img3,(1280,700))#width ,height
cv2.imshow("Original Image",img3)
print("Image in original value==\n",img3)

cv2.waitKey(0)  #here parameter inside waitkey handle the life duration of an image
cv2.destroyAllWindows()


#Image conversion project colored image into grayscale.

#path = input("Enter the Path and name of an image===")
#print("You Enter this===",path)

#Now read image 
img1 = cv2.imread("H:\\Data\\thor.jpg",0) #convert image into grayscale
img1 = cv2.resize(img1,(560,700))
img1 = cv2.flip(img1,0)#it accept 3 parameters 0,-1,1
cv2.imshow("converted image==",img1)
k = cv2.waitKey(0) & 0xFF
if k == ord("q"):
    cv2.destroyAllWindows()
    
elif k == ord("s"):
    cv2.imwrite("H:\\ouput.png",img1)  #it accept name of image and data
    cv2.destroyAllWindows()


 
























