# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 22:36:07 2021

@author: Admin
"""

import cv2

path = "E:/4-1/DIP/Image/city-lights-under-night-sky-771881.jpg"

img = cv2.imread(path)
width,height =400,400
imgResize=cv2.resize(img,(width,height))
print(img.shape)
print(imgResize.shape)
imgCropped= img[1000:1536,400:2304]
croppedImgResize = cv2.resize(imgCropped,(img.shape[1],img.shape[0]))
cv2.imshow("croppedImageResize",croppedImgResize)

cv2.waitKey()