from tkinter import X
import numpy
import PIL
import math
import time
import picamera
import numpy as np
import cv2
import matplotlib as plt
import io
from task3 import sobel


def make_circle(img,center,radius,colour):
    for x in range (center[0]-radius,center[0]+radius):
        for y in range (center[1]-radius,center[1]+radius):
            print(x,y)
            x_vector = x - center[0]
            y_vector = y - center[1]
            if ((x_vector * x_vector) + (y_vector * y_vector)) <= radius * radius:
                img[x,y]=colour
    return img
    
with picamera.PiCamera() as camera:
    camera.resolution=(320,240)
    time.sleep(3)
    camera.capture('assets/pi_photo')
image = cv2.imread('assets/pi_photo')

image = make_circle(image,(100,100),15,[0,0,0])
image = make_circle(image,(67,90),17,[255,60,50])
image = make_circle(image,(190,200),30,[89,255,150])
cv2.imshow('image', image)
sobeled = sobel(image)
cv2.imshow('sobeled', sobeled)
raw_key = cv2.waitKey(20000)
