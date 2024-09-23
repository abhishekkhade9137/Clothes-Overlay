import os

import cvzone
import cv2
from cvzone.PoseModule import PoseDetector


#cap = cv2.VideoCapture("C:\\Users\\abhis\\Music\\Projects\\Clothes\\Resources-1\\Resources\\Videos\\1.mp4")
#cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture("C:\\Users\\abhis\\Pictures\\Camera Roll\\WIN_20240918_16_16_53_Pro.mp4")
detector = PoseDetector()

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    scale_percent = 25  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    #img = cv2.flip(img, 1)
    imgshirt=cv2.imread("C:\\Users\\abhis\\Music\\Projects\\Clothes\\Resources-1\\Resources\\Shirts\\2.png",cv2.IMREAD_UNCHANGED)
    imgshirt = cv2.cvtColor(imgshirt, cv2.COLOR_RGB2RGBA)
    fixedRatio = 262 / 190 
    ratiohw=581 / 440
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
    
    if lmList:
        lm11=lmList[11]
        lm12=lmList[12]
        lm23=lmList[23]
        lm24=lmList[24]
        lm20=lmList[20]
        lm0=lmList[0]
        
        shirtwidth = int((lm11[0] - lm12[0]) * fixedRatio)
        print(shirtwidth)
        imgshirt=cv2.resize(imgshirt,(shirtwidth,int(shirtwidth*fixedRatio)))
        currentScale = (lm11[0] - lm12[0]) / 190
        offset = int(44 * currentScale), int(48 * currentScale)
        print(offset)
        img =cvzone.overlayPNG(img, imgshirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
        #img =cvzone.overlayPNG(img, imgshirt, (100,lm12[1]))
    cv2.imshow("Image", img)
    cv2.waitKey(1)