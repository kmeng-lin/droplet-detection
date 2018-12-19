# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:44:45 2018

@author: kevin
"""

import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt

img = cv.imread('6.15.18 wt Tau only 2pc PEG 10uM tiCtrl.tif',0)
outputpath='/home/kevin/Pictures/Thresh/'
if not os.path.exists(outputpath):
    os.mkdir(outputpath)
blur=cv.GaussianBlur(img, (5,5),0)
ret,thresh1 = cv.threshold(img,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
plt.imsave(outputpath+'thresh_otsu.png',thresh1,cmap='gray',format='png')
