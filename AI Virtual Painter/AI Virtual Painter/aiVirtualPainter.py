import cv2
import numpy as np
import cvzone
import os
import handTrackerModule as htm

######################
sekil_modu = ""
x,y,z = 0,0,0
r,g,b = 255,255,255
anlik_renk = x,y,z
thickness = 15
######################

success_status1=False
success_status2=False

status=""

blue =  cv2.imread("../blue.png")
red = cv2.imread("../red.png")
green =  cv2.imread("../green.png")

save = cv2.imread("../save.png")
trash= cv2.imread("../trash.png")
trash=cv2.resize(trash,(80,80))

blue = cv2.imread("../blue.png")
red = cv2.imread("../red.png")
green = cv2.imread("../green.png")

red=cv2.resize(red,(265,50))

blue= cv2.flip(blue,1)
red=cv2.flip(red,1)
green=cv2.flip(green,1)

kam = cv2.VideoCapture(0)
kam.set(3, 1280)
kam.set(4, 720)

daic1 , daic2 = 200 , 200
daix1 = daic1 - 140
daix2 = daic1 + 140
daiy1 = daic2 - 140
daiy2 = daic2 + 140

daic1v , daic2v = 200 , 500
daix1v = daic1v - 140
daix2v = daic1v + 140
daiy1v = daic2v - 140
daiy2v = daic2v + 140

kare = ""

sekil_modu=="çizim"

u=0
v=1
z1=0
l=[]
fl= tuple(enumerate(l))

detector = htm.handDetector(detectionCon=0.85)
xp, yp = 0,0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)
imgCanvasHsv=cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2HSV)
zamsın ="b"
while True:
    success, img = kam.read()
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (1280, 720))
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if zamsın =="b":
        imgCanvas = np.zeros((720, 1280, 3), np.uint8)
        cv2.rectangle(img, (426, 120 + 15), (596, 210 + 15), (128, 128, 128), cv2.FILLED)
        cv2.rectangle(img, (431, 125 + 15), (591, 205 + 15), (150, 150, 150), cv2.FILLED)
        cv2.putText(img, "Drawing", (460, 193), cv2.FONT_HERSHEY_COMPLEX, 1, (80, 80, 80), 2)

        cv2.rectangle(img, (686, 120 + 15), (855, 210 + 15), (128, 128, 128), cv2.FILLED)
        cv2.rectangle(img, (691, 125 + 15), (850, 205 + 15), (150, 150, 150), cv2.FILLED)
        cv2.putText(img, "Matching", (710, 193), cv2.FONT_HERSHEY_COMPLEX, 1, (80, 80, 80), 2)

        if len(lmList) != 0:
            # print(lmList)

            x0, y0 = lmList[4][1:]
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
            fingers = detector.fingersUp()
            # print(fingers)
            if fingers[0]==True and fingers[1]==False and fingers[2]==True:
                cv2.circle(img, (x1,y1) , 15, (x,y,z), cv2.FILLED)
            if (fingers[1] == False and fingers[2] == False):
                l.clear()
                u = 0
                v = 1
                xp, yp = 0, 0
                cv2.rectangle(img, (x1, y1 - 40), (x2, y2 + 29), (x, y, z), cv2.FILLED)
                print("Selection")
                if y1 <= 235 and y1 >= 150:

                    if x1>=426 and x1<596:
                        zamsın="c"
                    if x1>=686 and x1<= 885:
                        zamsın = "t"

    if zamsın == "c":

        cv2.rectangle(img, (0, 0), (85, 65), (128, 128, 128), cv2.FILLED)
        cv2.rectangle(img, (5, 5), (80, 60), (20, 30, 180), cv2.FILLED)
        cv2.putText(img, "X", (34,42), cv2.FONT_HERSHEY_COMPLEX, 1, (60, 60, 50), 2)

        cv2.rectangle(img, (241, 135), (305, 199), (128, 128, 128), 7)
        cv2.rectangle(img, (95, 120+15), (220, 210+15), (128, 128, 128), cv2.FILLED)
        cv2.rectangle(img, (100, 125+15), (215, 205+15), (150, 150, 150), cv2.FILLED)
        cv2.putText(img, "Silgi", (120, 178+15), cv2.FONT_HERSHEY_COMPLEX, 1, (80, 80, 80), 2)
    #brush thickness

        cv2.rectangle(img, (95, 250+30), (305, 315+30), (128, 128, 128), cv2.FILLED)
        cv2.rectangle(img, (95, 250+30), (165, 315+30), (100, 100, 100), 3)
        cv2.rectangle(img, (165, 250+30), (235, 315+30), (100, 100, 100), 3)
        cv2.rectangle(img, (235, 250+30), (305, 315+30), (100, 100, 100), 3)
        cv2.putText(img, "1", (120, 292+30), cv2.FONT_HERSHEY_COMPLEX, 1, (80, 80, 80), 2)
        cv2.putText(img, "2", (190, 292+30), cv2.FONT_HERSHEY_COMPLEX, 1, (80, 80, 80), 2)
        cv2.putText(img, "3", (260, 292+30), cv2.FONT_HERSHEY_COMPLEX, 1, (80, 80, 80), 2)

        cv2.rectangle(img, (95, 20), (305, 80), (128, 128, 128), cv2.FILLED)
        cv2.rectangle(img, (100, 25), (300, 75), (x, y, z), cv2.FILLED)
        cv2.putText(img, "Anlik Renk", (125, 100), cv2.FONT_HERSHEY_COMPLEX, 0.8, (80, 80, 80), 2)

        cv2.rectangle(img, (365, 20), (640, 80), (128, 128, 128), cv2.FILLED)
        img[25:75, 370:635] = blue

        cv2.rectangle(img, (650, 20), (925, 80), (128, 128, 128), cv2.FILLED)
        img[25:75, 655:920] = green

        cv2.rectangle(img, (935, 20), (1210, 80), (128, 128, 128), cv2.FILLED)
        img[25:75, 940:1205] = red

        #shapes
        cv2.rectangle(img, (900 + 95, 120+15), (900 + 340, 210+15), (108, 108, 108), cv2.FILLED)
        cv2.rectangle(img, (900 + 100, 125+15), (900 + 335, 205+15), (128, 128, 128), cv2.FILLED)
        cv2.rectangle(img, (900 + 173, 120+15), (900 + 179, 210+15), (108, 108, 108), cv2.FILLED)
        cv2.rectangle(img, (900 + 254, 120+15), (900 + 259, 210+15), (108, 108, 108), cv2.FILLED)
        cv2.rectangle(img, (900 + 112, 132+15), (900 + 162, 197+15), (x,y,z), 7)
        cv2.circle(img, (900 + 216, 166+15), 25, (x,y,z), 7)
        cv2.line(img, (1170,200+10), (1225, 125+20), (x,y,z), 4)

        img[135:199, 241:305] = save
        img[135+150:215+150, 241+900:321+900] = trash
        cv2.rectangle(img, (1136, 280), (1226, 370), (100, 100, 100), 5)


        if x == 0 and y == 0 and z == 0:
            cv2.rectangle(img, (100, 205 + 15), (215, 210 + 15), (50,50,50), 5)

        if thickness==15:
            cv2.rectangle(img, (100, 310+30), (160, 315+30), (50,50,50), 5)
        elif thickness==30:
            cv2.rectangle(img, (170, 310 + 30), (230, 315 + 30), (50,50,50), 5)
        elif thickness==45:
            cv2.rectangle(img, (240, 310 + 30), (300, 315 + 30), (50,50,50), 5)

        if sekil_modu=="Kare":
            cv2.rectangle(img, (1000, 205+15), (1073, 210+15), (50,50,50), 3)
        elif sekil_modu == "Daire":
            cv2.rectangle(img, (1079, 205 + 15), (1154, 210 + 15),(50,50,50), 3)
        elif sekil_modu == "line":
            cv2.rectangle(img, (1159, 205 + 15), (1240, 210 + 15), (50,50,50), 3)

        if len(lmList)!= 0:
            #print(lmList)

            x0, y0 = lmList[4][1:]
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
            fingers = detector.fingersUp()
            #print(fingers)

            if (fingers[1] == False and fingers[2] == False):
                l.clear()
                u = 0
                v = 1
                xp, yp = 0, 0
                cv2.rectangle(img, (x1, y1 - 40), (x2, y2 + 29), (x, y, z), cv2.FILLED)
                print("Selection")
                if y1 < 315+30  and y2 < 315+30:
                    if y1 < 80 and y2 < 80:
                        if (365 < x1) and (x1 < 620):
                            x = x1 - (20 + 300)
                            print(x)

                        elif (650 < x1) and (x1 < 925):
                            y = x1 - (350 + 300)
                        elif (935 < x1) and (x1 < 1210):
                            z = x1 - (655 + 300)
                            print(z)
                    elif 120+15 < y1 < 210+15 and 120+15 < y2 < 210+15:
                        if 95 < x1 < 220:
                            x,y,z = 0,0,0
                        elif 241 < x1 < 305:
                            cv2.imwrite("ai_painter_save.png", imgCanvas)
                            cv2.putText(img, ("Sekliniz Kaydedildi"), (100, 255), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 80, 150), 1)
                        elif 1012 < x1 < 1062:
                            sekil_modu = "Kare"
                        elif 1091 < x1 < 1145:
                            sekil_modu = "Daire"
                        elif 1150 < x1 < 1240:
                            sekil_modu = "line"
                    elif 250+30 < y1 < 315+30 and 250+30 < y2 < 315+30:
                        if 95 < x1 < 165:
                            thickness = 15
                        elif 165 < x1 < 235:
                            thickness = 30
                        elif 235 < x1 < 305:
                            thickness = 45

                if x1 <= 100 and y1 <= 80:
                    zamsın = "b"

                if y1>=270 and y1<=375 and x1>=1130 and x1<=1230:
                    cv2.rectangle(imgCanvas,(0,0),(1280,720),(0,0,0),cv2.FILLED)

            if fingers[0]==True and fingers[1]==False and fingers[2]==True:
                cv2.circle(img, (x1,y1) , 15, (x,y,z), cv2.FILLED)
                print("Çizim Mode")
                if xp==0 and yp==0:
                    xp,yp = x1,y1
                if (x,y,z)==(0,0,0):
                    cv2.line(img, (xp, yp), (x1, y1), (x,y,z), thickness)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), (x,y,z), thickness)
                else:
                    cv2.line(img, (xp, yp), (x1,y1), (x,y,z),thickness )
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), (x,y,z), thickness)
                xp, yp = x1, y1
                l_element=xp,yp

                l.append(l_element)
                print(len(l))

            if fingers[0] == False and fingers[1] == True and fingers[2] == True and fingers[2] == True and fingers[3] == True:
                cv2.circle(img, (x0, y0), 15, (x, y, z), cv2.FILLED)
                print("kaplama")
                print(l)
                for i in l:
                  cv2.line(imgCanvas, (i), (x0, y0,), (x, y, z), 20)


            if fingers[0]==False and fingers[1]==False:
                if sekil_modu == "Kare":
                    cv2.rectangle(img, (x0,y0), (x1,y1), (x,y,z), 3)
                    if fingers[0]==False and fingers[1]==False and fingers[4]==False:
                        cv2.rectangle(img, (x0, y0), (x1, y1), (x, y, z), 3)
                        cv2.rectangle(imgCanvas, (x0, y0), (x1, y1), (x, y, z), 3)
                        sekil_modu = "Çizim"
                        print(sekil_modu)

                elif sekil_modu == "Daire":
                    cv2.circle(img, (x0,y0), int((((x1-x0)/6.5)**2 + ((y1-y0)/6.5)**2)**1/2), (x,y,z), 3)
                    if fingers[0]==False and fingers[1]==False and fingers[4]==False:
                        cv2.circle(img, (x0,y0), int((((x1-x0)/6.5)**2 + ((y1-y0)/6.5)**2)**1/2), (x,y,z), 3)
                        cv2.circle(imgCanvas, (x0,y0), int((((x1-x0)/6.5)**2 + ((y1-y0)/6.5)**2)**1/2), (x,y,z), 3)
                        sekil_modu = "Çizim"

                elif(sekil_modu=="line"):
                    if xp == 0 and yp == 0:
                        xp, yp = x1, y1
                    cv2.line(img, (x1, y1), (x0, y0), (x, y, z), thickness)
                    if fingers[0] == False and fingers[1] == False and fingers[4] == False:
                        cv2.line(img, (x1, y1), (x0, y0), (x, y, z), thickness)
                        cv2.line(imgCanvas, (x1, y1), (x0, y0), (x, y, z), thickness)
                        sekil_modu="Çizim"

    if zamsın=="t":

        l.clear()

        cv2.circle(imgCanvas, (1100, 180), 160, (220, 0, 0), cv2.FILLED)
        cv2.circle(img, (1100,180), 160, (220, 0, 0),15)

        cv2.circle(imgCanvas, (1100, 540), 160, (0, 200, 0), cv2.FILLED)
        cv2.circle(img, (1100, 540), 160, (0, 200, 0), 15)

        cv2.rectangle(img, (0, 0), (85, 65), (128, 128, 128), cv2.FILLED)
        cv2.rectangle(img, (5, 5), (80, 60), (20, 30, 180), cv2.FILLED)
        cv2.putText(img, "X", (34, 42), cv2.FONT_HERSHEY_COMPLEX, 1, (60, 60, 50), 2)

        if len(lmList)!= 0:
            #print(lmList)

            x0, y0 = lmList[4][1:]
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
            x3,y3 = lmList[20][1:]
            fingers = detector.fingersUp()
            if fingers[1] == False and fingers[2] == False:
                xp, yp = 0, 0
                status="idle"
                cv2.rectangle(img, (x1, y1 - 40), (x2, y2 + 29), (r, b, g), cv2.FILLED)
                print("boşta")

                if daix1 < x1 < daix2 and daiy1 < y1 < daiy2:
                    dai_uzakx1 = x1 - daix1
                    dai_uzakx2 = daix2 - x1
                    dai_uzaky1 = y1 - daiy1
                    dai_uzaky2 = daiy2 - y1
                if daix1v < x1 < daix2v and daiy1v < y1 < daiy2v:
                    dai_uzakx1v = x1 - daix1v
                    dai_uzakx2v = daix2v - x1
                    dai_uzaky1v = y1 - daiy1v
                    dai_uzaky2v = daiy2v - y1

            if fingers[1] == False and fingers[2] == True:
                cv2.circle(img, (x1, y1), 15, (r, b, g), cv2.FILLED)
                status="carrying"
                print("taşıma")

                if daix1 < x1 < daix2 and daiy1 < y1 < daiy2:
                    daix1 = x1 - dai_uzakx1
                    daix2 = x1 + dai_uzakx2
                    daiy1 = y1 - dai_uzaky1
                    daiy2 = y1 + dai_uzaky2
                    daic1 = x1
                    daic2 = y1
                    imgCanvas = np.zeros((720, 1280, 3), np.uint8)

                    cv2.circle(imgCanvas, (1100, 180), 160, (220, 0, 0), cv2.FILLED)
                    cv2.circle(img, (1100, 180), 160, (220, 0, 0), 15)
                    cv2.circle(imgCanvas, (1100, 540), 160, (0, 200, 0), cv2.FILLED)
                    cv2.circle(img, (1100, 540), 160, (0, 200, 0), 15)

                if daix1v < x1 < daix2v and daiy1v < y1 < daiy2v:
                    daix1v = x1 - dai_uzakx1v
                    daix2v = x1 + dai_uzakx2v
                    daiy1v = y1 - dai_uzaky1v
                    daiy2v = y1 + dai_uzaky2v
                    daic1v = x1
                    daic2v = y1
                    imgCanvas = np.zeros((720, 1280, 3), np.uint8)

                    cv2.circle(imgCanvas, (1100, 540), 160, (0, 200, 0), cv2.FILLED)
                    cv2.circle(img, (1100, 540), 160, (0, 200, 0), 15)
                    cv2.circle(imgCanvas, (1100, 180), 160, (220, 0, 0), cv2.FILLED)
                    cv2.circle(img, (1100, 180), 160, (220, 0, 0), 15)

                if x1<= 100 and y1<=80:
                    zamsın = "b"


        denemedaire = cv2.circle(imgCanvas, (daic1, daic2), 150, (220,0,0), cv2.FILLED)
        denemedaire = cv2.circle(img, (daic1, daic2), 150, (220, 0, 0), 20)

        denemedairev = cv2.circle(imgCanvas, (daic1v, daic2v), 150, (0, 220, 0), cv2.FILLED)
        denemedairev = cv2.circle(img, (daic1v, daic2v), 150, (0, 220, 0), 20)

        if status=="idle" and daic1 <=1170 and daic1 >= 1030 and daic2<=200:
            success_status1=True

        if status == "idle" and daic1v <= 1170 and daic1v >= 1030 and daic2v >= 500:
            success_status2=True
            print ("oke")

        if success_status1 == True:
          cv2.circle(img, (1100, 180), 160, (0, 220, 0), 20)
        elif success_status2 ==True:
         cv2.circle(img,  (1100, 540) , 160, (0, 220, 0), 20)
        if success_status1==True and success_status2==True:
         zamsın="b"

    imgCanvas = cv2.resize(imgCanvas, (1280, 720))
    img = cv2.addWeighted(img, 0.7, imgCanvas, 0.5, 0)
    cv2.imshow("Resim" , img)
    #cv2.imshow("Canvas", imgCanvas)
    cv2.waitKey(1)


kam.release()
cv2.destroyAllWindows()
