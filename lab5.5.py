import numpy
import PIL
import math
import time
import picamera
import numpy as np
import cv2
import matplotlib as plt
import io

stream=io.BytesIO()
with picamera.PiCamera() as camera:
	camera.resolution=(320,240)
	camera.framerate=24
	time.sleep(1)
	camera.capture(stream,format='jpeg')
data=np.fromstring(stream.getvalue(),dtype=np.uint8)
image=cv2.imdecode(data,1)

# with picamera.PiCamera() as camera:
#     camera.resolution=(320,240)
#     time.sleep(3)
#     camera.capture('assets/pi_photo')
#     image = cv2.imread('assets/pi_photo')

window_name = 'lab 5.2'

cv2.imshow(window_name, image)
raw_key = cv2.waitKey(1000)

image[120,64]=0,128,255

window_name2 = 'lab 5.5 orange'
cv2.imshow(window_name2, image)
raw_key = cv2.waitKey(20000)
