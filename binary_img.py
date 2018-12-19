# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:33:40 2018

@author: kevin
"""
import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt

img = cv.imread('/home/kevin/Pictures/Denoised/denoised3.png',0)
#img=cv.imread('/home/kevin/Pictures/new_img.png', 0)
outputpath='/home/kevin/Pictures/Thresh/'
if not os.path.exists(outputpath):
    os.mkdir(outputpath)
for i in range(50,90):
#for i in range(150,180):
    ret,thresh1 = cv.threshold(img,i,255,cv.THRESH_BINARY_INV)
    plt.imsave(outputpath+'thresh'+str(i)+'.png',thresh1,cmap='gray',format='png')

#create for-loop testing various thresholds (70-90)
