from djitellopy import tello
import cv2
import numpy as np

width = 640
height = 480
deadZone = 100

startCounter = 0

me = Tello()
me.connect()
me.for_back_velocity = 0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0

print(me.get_battery())

me.streamoff()

me.streamon()


frameWidth = width
frameHeight = height

global imgContour
global dir
def empty(a):
    pass


cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE Min","HSV",20,179,empty)
cv2.createTrackbar("HUE Max","HSV",40,179,empty)
cv2.createTrackbar("SAT Min","HSV",148,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VALUE Min","HSV",89,255,empty)
cv2.createTrackbar("VALUE Max","HSV",255,255,empty)

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
for x in range (0, rows):
    for y in range(0, cols):
        if imgArray[x][y],shape[:2] == imgArray[0][0].shape[:2]:
            imgArray[x][y] = cv2.resize(imgArray[x][y], (0,0), None, scale, scale)
            else:
                imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
                imageBlank = np.zeros((height, width, 3), np.uint8)
                hor = [imageBlank]*rows
                hor_con = [imageBlank]*rows
                for x in range(0, rows):
                    hor[x] = np.hstack(imgArray[x])

                    ver = np.vstack(hor)
                    else:
                        for x in range(0, rows):
                            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
                                else:
                                    imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
                                    if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
                                    hor = np.hstack(imgArray)
                                    ver = hor
                                    return ver


                                    def getContours(img, imgContour):
                                        global dir

                                        contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                                        for cnt in contours:
                                            area = cv2.contourArea(cnt)
                                            areaMin = cv2.getTrackbarPos("Area", "Parameters")
                                            if area > areaMin:
                                                cv2.drawContours(imgContour, cnt, -1(255, 0, 255), 7)
                                                peri = cv2.arcLength(cnt, True)
                                                approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)




                                                x , y , w , h = cv2.boundingRect(approx)
                                                cx = int(x + (w / 2))
                                                cy = int(y +(h / 2))

                                                if (cx <int(frameWidth/2)-deadZone):
                                                    cv2.putText(imgContour, "Go left", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
                                                    cv2.rectangle(imgContour,(0, int(frameHeight/2-deadZone)),(int(frameWidth/2)-deadZone, int(frameHeight/2)+deadZone),(0,0,255), cv2.FILLED)
                                                    dir = 1

                                                    elif (cx > int(frameWidth / 2) + deadZone):
                                                    cv2.putText(imgContour, "Go right", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
                                                    cv2.rectangle(imgContour,(int(frameWidth/2+deadZone),int(frameHeight/2-deadZone)),(frameWidth,int(frameHeight/2)+deadZone),(0,0,255), cv2.FILLED)
                                                    dir = 2

                                                    elif  (cy < int(frameHeight / 2)- deadZone):
                                                        cv2.putText(imgContour, "Go up", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
                                                        cv2.rectangle(imgContour,(int(frameWidth/2-deadZone), int(frameHeight/2)+deadZone),(int(frameWidth/2+deadZone),frameHeight),(0,0,255),cv2.FILLED)
                                                        dir = 3
                                                      
                                                      elif (cy > int(frameHeight / 2) + deadZone):
                                                        cv2.putText(imgContour, "Go down", (20, 50) cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255), 3)
                                                        cv2.rectangle(imgContour,(int(frameWidth/2-deadZone), int(frameHeight/2)+deadZone),(int(frameWidth/2+deadZone),frameHeight),(0,0,255),cv2.FILLED)
                                                        else: dir=0
                                                        





