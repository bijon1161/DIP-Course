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
cv2.imshow("City",img)
cv2.imshow("City",imgResize)
cv2.waitKey()