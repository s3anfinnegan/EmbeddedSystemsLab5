import numpy
import PIL
import math
import time
import picamera
import numpy as np
import cv2
import matplotlib as plt
import io


def make_square(img,upper_left,size,colour):
    for x in range (upper_left[0],upper_left[0]+size):
        for y in range (upper_left[1],upper_left[1]+size):
            img[x,y]=colour
    return img

with picamera.PiCamera() as camera:
    camera.resolution=(320,240)
    time.sleep(3)
    camera.capture('assets/pi_photo')
    image = cv2.imread('assets/pi_photo')

image =cv2.imread('assets/0_Screen-Shot-2020-08-21-at-163535.png')
image = cv2.resize(image, (320,240))

image = make_square(image,(5,10),9,[0,0,0])
image = make_square(image,(67,90),12,[255,60,50])
image = make_square(image,(190,200),30,[89,255,150])

cv2.imshow('window_name2', image)
raw_key = cv2.waitKey(20000)
