import mediapipe as mp
import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

## define hand detector, with 0.8 probability (to avoid push random key)
detector=HandDetector(detectionCon=0.8)

while True:
    ## open the web cam
    success, img=cap.read()
    
    # img=detector.findHands(img)
    # lmList,bboxInfo=detector.findPosition(img)
    hands,img=detector.findHands(img)
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"] # List of 21 Landmarks 
   
    cv2.rectangle(img,(100,100),(200,200),(255,0,255),cv2.FILLED)
    cv2.putText(img,"Q",(115,180),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
