import cv2  # opencv-python ver  4.5.3.56
from cvzone.HandTrackingModule import HandDetector   # cvzone ver 1.5.1

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)


while True:
    # open the web cam
    success, img = cap.read()
    hands, img = detector.findHands(img)  # With draw
    # hands=detector.findHands(img, draw=False) # No draw

    # Hands is list and each Hand is a dictinary with has tgis information:
    # Hand - dict (lmList - bbox - center - type)

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbond1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1["center"]  # Center of the hand cx,cy
        handType1 = hand1["type"]  # Hand type Left or Right

        fingers1 = detector.fingersUp(hand1)

        # Distance
        # length,info,img=detector.findDistance(lmList1[8],lmList1[12],img)
        # length,info=detector.findDistance(lmList1[8],lmList1[12]) # no draw

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmarks points
            bbond2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2["center"]  # Center of the hand cx,cy
            handType2 = hand2["type"]  # Hand type Left or Right

            fingers2 = detector.fingersUp(hand2)

            # print(fingers1,fingers2)

            # length,info,img=detector.findDistance(lmList1[8],lmList2[8],img)
            length, info, img = detector.findDistance(
                centerPoint1, centerPoint2, img)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
