# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 14:06:50 2018

@author: kevin
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('6.15.18 wt Tau only 2pc PEG 10uM tiCtrl.tif',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
 
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
cv2.imwrite('res.png',res)

new_img = cv2.imread('a.tif',0)
mask=new_img.copy()
mask.fill(4)
new_img=cv2.multiply(new_img,mask)
np.clip(new_img,0,210,new_img)
nmask=mask.copy()
nmask.fill(50)
new_img=cv2.subtract(new_img,nmask)
cv2.imwrite('res2.png', new_img)