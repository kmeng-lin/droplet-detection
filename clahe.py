# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:23:24 2018

@author: kevin
"""

import numpy as np
import cv2

img = cv2.imread('/home/kevin/Pictures/Denoised/denoised3.png',0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE()
cl1 = clahe.apply(img)

cv2.imwrite('clahe_2.png',cl1)
