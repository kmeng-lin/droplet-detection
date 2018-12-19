# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 19:46:59 2018

@author: kevin
"""

import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt
img = cv.imread('a.tif') #replace with image name


outputpath='/home/kevin/Pictures/Denoised/'
if not os.path.exists(outputpath):
    os.mkdir(outputpath)
for i in range(1,10):
	dst = cv.fastNlMeansDenoising(img,None,i,7,21)
	plt.imsave(outputpath+'denoised'+str(i)+'.png',dst)
