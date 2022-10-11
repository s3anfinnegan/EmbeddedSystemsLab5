import numpy as np
import cv2 as cv

filename = 'assets/house.jpg'
img = cv.imread(filename)
img = cv.resize(img, (0,0), fx=2,fy=2) 
height,width,channels=img.shape #get the image height and width
import numpy as np
import cv2 as cv

filename = 'assets/house.jpg'
img = cv.imread(filename)
img = cv.resize(img, (0,0), fx=2,fy=2) #Increasing image size 2x
height,width,channels=img.shape #get the image height and width
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) #create a grey scale version of our image for our detector to run over

# arrived at these numbers through experimentation
# the params are as follows the image, 
# Size of blocks to be detected for corners Larger the number the larger the area of pixels which will be checked and thus highlighted
# ksize As the Kernel size increases, more pixels are now a part of the convolution process. This signifies that the gradient map (edges) will tend to get blurry to a point the output looks likes a plastic cover has been wrapped around the edges. 
# K allows you to influence the precision so higher value less false flags more actuals missed 0.1 chosen given desired number of large corners
dst = cv.cornerHarris(gray,3,1,0.1)

# result is dilated for marking the corners, not important
# In simple terms makes the corners fatter to be seen easy, More iterations = fatter
# dilation adds pixels to the corners of objects to allow the visual insepction of the object to be done more easily
dst = cv.dilate(dst,None,iterations=1)

# This makes img an array with the same height and width and one channel which makes it a completely black greyscaled image. 
img = np.zeros((height,width,1), np.uint8)

# Threshold for an optimal value based on our target our threshold value is very low to allow a large number of corners
# dst.max gives the max confidence over the entire image. 
# we are selecting corners if their confidence variable is greater than 0.0001% of that max confidence for this image. 
# these pixels are then set to white on our fully black image from above
img[dst>0.000001*dst.max()]=[255]
cv.imshow('dst',img)
cv.waitKey(0)
import numpy as np
import cv2 as cv

filename = 'assets/house.jpg'
img = cv.imread(filename)
img = cv.resize(img, (0,0), fx=2,fy=2) 
height,width,channels=img.shapeimg = cv.resize(img, (0,0), fx=2,fy=2) 
ray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) 

dst = cv.cornerHarris(gray,3,1,0.1)

dst = cv.dilate(dst,None,iterations=1)

img = np.zeros((height,width,1), np.uint8)

img[dst>0.000001*dst.max()]=[255]
cv.imshow('dst',img)
cv.waitKey(0)
