import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self,mode=False, maxHands=2, modelCom=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelCom = modelCom
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands, self.modelCom ,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                u, g, k = img.shape
                kx, ky = int(lm.x * g), int(lm.y * u)
                self.lmList.append([id, kx, ky])
                if draw:
                    cv2.circle(img, (kx, ky), 15, (255, 0, 255), cv2.FILLED)
        return self.lmList

    def fingersUp(self):
        fingers = []

        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1,5):
            if self.lmList[self.tipIds[id]][2] > self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers


def main():
    cam = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cam.read()
        img = detector.findHands(img)
        detector.findPosition(img)

        cv2.imshow("Cam", img)
        if (cv2.waitKey(1) & 0xFF == ord("q")):
            cam.set(1280, 720)
            break
if __name__ == "__main__":
    main()
