import cv2  # opencv-python  4.5.3.56
from cvzone.HandTrackingModule import HandDetector  # cvzone  1.5.1
from time import sleep
import numpy as np
import cvzone
from pynput.keyboard import Controller  # pynput 1.7.3

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# define hand detector, with 0.8 probability (to avoid push random key)
detector = HandDetector(detectionCon=0.8)
keys = [["Q", "W", "E", "R", "T", "Y", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "H", ",", ".", "/"]]
finalText = ""
keyboard = Controller()


def drawIt(img, btnStartPos, btnEndPos, btnColor, btnText, btnTextStartPos, btnTextColor, btnTextFontScale, btnTextFontThikness):
    cv2.rectangle(img, btnStartPos, btnEndPos, btnColor, cv2.FILLED)
    cv2.putText(img, btnText, btnTextStartPos, cv2.FONT_HERSHEY_PLAIN,
                btnTextFontScale, btnTextColor, btnTextFontThikness)
    return img


def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (x, y, w, h), 20, rt=0)
        drawIt(img, button.pos, (x+w, y+h), (255, 0, 255),
               button.text, (x+20, y+65), (255, 255, 255), 4, 4)
    return img


# def drawAllFancy(img, buttonList):
#     imgNew = np.zeros_like(img, np.uint8)
#     for button in buttonList:
#         x, y = button.pos
#         cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
#                           20, rt=0)
#         drawIt(imgNew, button.pos, (x + button.size[0], y + button.size[1]), (
#             255, 0, 255), button.text, (x + 40, y + 60), (255, 255, 255), 2, 3)

#     out = img.copy()
#     alpha = 0.5
#     mask = imgNew.astype(bool)
#     # print(mask.shape)
#     out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
#     return out


class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text


buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

while True:
    # open the web cam
    success, img = cap.read()

    # img=detector.findHands(img)
    # lmList,bboxInfo=detector.findPosition(img)

    hands, img = detector.findHands(img)
    img = drawAll(img, buttonList)
    if hands:
        # Hand 1e
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks

        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmList1[8][0] < x+w and y < lmList1[8][1] < y+h:
                drawIt(img, (x-5, y-5), (x+w+5, y+h+5), (175, 0, 175),
                       button.text, (x+20, y+65), (255, 255, 255), 4, 4)
                l, _ = detector.findDistance(lmList1[8], lmList1[12])

                # When clicked
                if l < 40:
                    keyboard.press(button.text)
                    drawIt(img, button.pos, (x+w, y+h),  (0, 255, 0),
                           button.text, (x+20, y+65), (255, 255, 255), 4, 4)
                    finalText += button.text
                    sleep(0.30)

    drawIt(img, (50, 350), (700, 450), (175, 0, 175),
           finalText, (60, 430),  (255, 255, 255), 5, 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
