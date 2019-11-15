import numpy as numpy
import cv2
from PIL import Image
import os
import skimage
from skimage.feature import daisy
from skimage import data
import matplotlib.pyplot as plt
import csv



img = cv2.imread('4.png',0)
res = cv2.resize(img,(32,32))
cv2.imwrite('resized.png',res)
img = skimage.io.imread('resized.png')


modified_arr = []
for rows in img:
	temp_row = []
	for val in rows:
		if(val == 255):
			temp_row.append(0)
		else:
			temp_row.append(1)
	modified_arr.append(temp_row)
	temp_row = []
    
    
Matrix = numpy.array(modified_arr)
temp_a, temp_b = numpy.vsplit(Matrix,2)
one_a, two_a = numpy.hsplit(temp_a,2)
three_a, four_a = numpy.hsplit(temp_b,2)

sub_matrices = [one_a,two_a,three_a,four_a]
shadow_vector = []
for val in sub_matrices:
    s,e,m,n,p,k,f=0,0,0,0,0,0,0
    
    for row in range(0,16):
        for col in range(0,16):
            if(val[row][col]==1):
                k=k+1
                s=s+col
        if(k!=0):
            f=s/k
            m=m+f
        k=0
        s=0
        
    
    
    for col in range(0,16):
        for row in range(0,16):
            if(val[row][col]==1):
                k=k+1
                p=p+row
        if(k!=0):
            e=p/k
            n=n+e
        k=0
        p=0
  
    shadow_vector.append(m/16)
    shadow_vector.append(n/16)

