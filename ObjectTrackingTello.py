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