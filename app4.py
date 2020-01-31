# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 22:24:21 2019

@author: ashto
"""
import matplotlib.pyplot as plt
import numpy as np
#Enter file name
name = input("Enter compressed coordinate matrix file name: ")
A = np.loadtxt(name)
#separate each column into its own array
row_index = A[:,0]
column_index = A[:,1]
values = A[:,2]
#initialize image array
image = np.zeros((int(np.max(column_index))+1,int(np.max(row_index))+1))
#fill image array with correct values
for i in range(len(column_index)):
    x=int(column_index[i])
    y=int(row_index[i])
    image[x,y] = values[i]
#plot the array
plt.imshow(image,cmap="binary")
plt.show()