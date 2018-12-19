# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 12:37:02 2018

@author: kevin
"""

import cv2
import numpy as np
import sys

#Import the image
img=cv2.imread('/home/kevin/Pictures/Thresh/thresh72.png',0)

#remove bubbles and prepare for analysis
img_clone=img.copy()

nr, nc=img.shape
img=img.astype(int)

#Create a cropped version of the image
#img = img[325:375, 325:375]
#img = img[300:400, 300:400]
#cv2.imwrite('/home/kevin/Documents/droplet images/Erosion/thresh78_crop.png',img)

#Edit the image values so they are each a different number
value=1
for r in range(nr):
    for c in range(nc):
        if img[r][c] == 255:
            img[r][c]=value
            value+=1

#np.set_printoptions(threshold=np.inf, linewidth=np.inf)  # turn off summarization, line-wrapping
#with open('/home/kevin/Documents/droplet images/text.txt', 'w') as f:
    #f.write(np.array2string(img, separator=', '))

#Create a while loop to normalize the value of each grouping with the largest value(neighbors above and below)
#Loop stops when no more changes can be made
change_count=1; #increases in value everytime there is a number change
while(change_count!=0): 
    change_count=0
    for r in range(nr):
        for c in range(nc):
            if img[r][c] is not 0: #rules out comparison with any black pixels
                if r!=0:
                    if img[r-1][c]<img[r][c] and img[r-1][c]!=0:
                        change_count+=1
                        img[r][c]=img[r-1][c]
                if r!=nr-1:
                    if img[r+1][c]<img[r][c] and img[r+1][c]!=0:
                        change_count+=1
                        img[r][c]=img[r+1][c]
                if c!=0:
                    if img[r][c-1]<img[r][c] and img[r][c-1]!=0:
                        change_count+=1
                        img[r][c]=img[r][c-1]
                if c!=nc-1:
                    if img[r][c+1]<img[r][c]and img[r][c+1]!=0:
                        change_count+=1
                        img[r][c]=img[r][c+1]
#end while
                        
                        
#np.set_printoptions(threshold=np.inf, linewidth=np.inf)  # turn off summarization, line-wrapping
#with open('/home/kevin/Documents/droplet images/test.txt', 'w') as f:
   # f.write(np.array2string(img, separator=', '))


keys,values =np.unique(img,return_counts=True)
dicts = dict(zip(keys, values))
keys=list(keys)
#filter out 0s and values less than 10
del dicts[0]
keys.remove(0)
l=list()
for number in dicts.keys():
    count=dicts[number]
    if count<10 or number==0:
        l.append(number)
for k in l: 
    del dicts[k]
    keys.remove(k)    
    
#creates necessary lists to store anchor box coordinates
upper=[]
lower=[]
left=[]
right=[]

#loops through the image to find coordinates of starting and end pixel coordinates for each object
temp_x=[]
temp_y=[]
for obj in keys:
    for r in range(nr):
        if obj in img[r]:
            temp_x.append(r)
    upper.append(temp_x[0])
    lower.append(temp_x[-1])
    temp_x[:]=[]
    for c in range(nc):
        if obj in img.T[c]:
            temp_y.append(c)
    left.append(temp_y[0])
    right.append(temp_y[-1])
    #if temp_y[-1]==1343 : 
        #print(temp_y)
        #input()
    temp_y[:]=[]    

#create anchor box coordinates
coordinates=zip(left,right,upper,lower)
anchor_boxes=dict(zip(keys,coordinates))

#for i in range(len(lower)):
    #lower[i]+=5
    #if lower[i]>1023:
       # lower[i]=1023
    
#load original
original=cv2.imread('6.15.18 wt Tau only 2pc PEG 10uM tiCtrl.tif')

#draw boxes
for i in range(len(upper)):     
    original[upper[i], left[i]:right[i]]=255 #draws upper edge
    original[upper[i]:lower[i], left[i]]=255  #draws left edge
    original[lower[i], left[i]:right[i]]=255  #draws bottom edge
    original[upper[i]:lower[i], right[i]]=255  #draws right edge
cv2.imwrite("img.png",original)

     

             

            
            
        
