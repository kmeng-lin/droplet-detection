# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 14:03:24 2018

@author: kevin
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('/home/kevin/Pictures/Denoised/denoised3.png',0)
hist,bins=np.histogram(img.flatten(),256,[0,256])
plt.hist(img.flatten(),256,[0,256])

alpha=2.3
beta=0

new_image = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
cv2.imwrite('new_img.png',new_image)
plt.hist(new_image.flatten(),256,[0,256])
equ=cv2.equalizeHist(img)
cv2.imwrite('equ.png',equ)
