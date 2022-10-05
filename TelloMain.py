from djitellopy import tello
import cv2
import time

width = 320
height = 240
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

while True:
    frame_read = me.get_frame_read()
    myFrame = frame_read.frame
    img = cv2.resize(myFrame, (width, height))

    if startCounter == 0:
        me.takeoff()
        time.sleep(8)
        me.rotate_clockwise(90)
        time.sleep(3)
        me.move_left(35)
        time.sleep(3)
        me.land()
        startCounter = 1

        cv2.imshow("MyResult", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            me.land()
            break