from djitellopy import tello
import cv2
import time

width = 320
height = 240
startCounter = 0


me = Tello()
me.connect()
me.for_back_velocity = 0
