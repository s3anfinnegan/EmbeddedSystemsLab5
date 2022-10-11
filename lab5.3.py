import numpy
import PIL
import math
import time
import picamera
import numpy as np
import cv2
import matplotlib as plt
import io

def sobel():
	window_name = 'task 1.3'
	cv2.imshow(window_name, image)
	raw_key = cv2.waitKey(5000)
	image2=image
	height,width,channels=image.shape
	for x in range (1,height-1):
		for y in range (1,width-1):
			Gx=0
			Gy=0
			r,g,b=image[x-1,y-1]
			int=(r+g+b)
			Gx+=-int
			Gy+=-int
			r,g,b=image[x-1,y]
			Gx+=-2*(r+g+b)
			r,g,b=image[x-1,y+1]
			Gx+=-(r+g+b)
			Gy+=(r+g+b)
			r,g,b=image[x,y-1]
			Gy+=-2*(r+g+b)
			
			r,g,b=image[x,y+1]
			Gy+=-2*(r+g+b)
			
			r,g,b=image[x+1,y-1]
			Gx+=(r+g+b)
			Gy+=-(r+g+b)
			r,g,b=image[x+1,y]
			Gx+=2*(r+g+b)
			r,g,b=image[x+1,y+1]
			Gx+=(r+g+b)
			Gy+=(r+g+b)
			length=math.sqrt((Gx*Gx)+(Gy*Gy))
			length=length/4328*255
			length=numpy.floor(length)
			image2[x,y]=length,length,length
	return image2

	

if __name__ == "__main__":
	# stream=io.BytesIO()
	# with picamera.PiCamera() as camera:
	# 	camera.resolution=(320,240)
	# 	camera.framerate=24
	# 	time.sleep(1)
	# 	camera.capture(stream,format='jpeg')
	# data=np.fromstring(stream.getvalue(),dtype=np.uint8)
	# image=cv2.imdecode(data,1)

	with picamera.PiCamera() as camera:
		camera.resolution=(320,240)
		time.sleep(3)
		camera.capture('assets/pi_photo')
		image = cv2.imread('assets/pi_photo')

	# image = cv2.imread('assets/0_Screen-Shot-2020-08-21-at-163535.png')

	sobel(image)
	window_name2 = 'Sobel filter'
	cv2.imshow(window_name2, image)
	raw_key = cv2.waitKey(20000)
