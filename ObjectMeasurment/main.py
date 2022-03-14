import cv2
import numpy as np
import utils


###########
webcam=False
path='/Users/piroova/Downloads/2.jpg' 
cap=cv2.VideoCapture(0)
cap.set(10,160)
cap.set(3,1920)
cap.set(4,1080)


while True:
    # if webcame is True it will show the camera picture
    #  otherwise it will read an show the image saved in path
    if webcam:success,img=cap.read()
    else: img=cv2.imread(path)

    # call getContours to have Canny image
    img,finalContures=utils.getContours(img,showCanny=True,draw=True)

    # resize the image (scale down) for big images (if the image saved in path is big, and it can't be shown completly)
    img=cv2.resize(img,(0,0),None,0.5,0.5)
    # success,img=cap.read()
    cv2.imshow('Original',img)
    cv2.waitKey(1)

