# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:13:37 2018

@author: kevin
"""
import os
import cv2
import numpy as np
import glob
from matplotlib import pyplot as plt


outputpath='/home/kevin/Pictures/Erosion/'
if not os.path.exists(outputpath):
    os.mkdir(outputpath)
#names=glob.glob('/home/kevin/Pictures/Thresh/*')
names=glob.glob('/home/kevin/Pictures/thresh_otsu.png')
for name in names:
    bn=os.path.basename(name)
    newname=os.path.join(outputpath, bn)
    img = cv2.imread(name, 0)
    kernel = np.ones((5,5), np.uint8)
    img_erosion = cv2.erode(img, kernel, iterations=1)
    plt.imsave(newname,img_erosion, cmap='gray', format='png')
    cv2.waitKey(0)
 

