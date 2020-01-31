# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 17:07:50 2019

@author: ashto
"""
import numpy as np
import matplotlib.pyplot as plt

#initialize variables, lists and matrices
n = input("Newton fractal z**n=1, Enter n (default 3): ")
start_min_max = input("Enter xmin,xmax,ymin,ymax (default -1.35,1.35,-1.35,1.35): ")
if n == "":
    n = 3
else:
    n = int(n)
if start_min_max == "":
    xmin,xmax,ymin,ymax = -1.35,1.35,-1.35,1.35
else:
    xmin,xmax,ymin,ymax = map(float, start_min_max.split())
sol = []
minimum = []
x = np.linspace(xmin+0.0011,xmax,1000)
y = np.linspace(ymin+0.0011,ymax,1000)
C = np.zeros((1000,1000),dtype=complex)
int_matrix = np.zeros((1000,1000))
#calculate,store,and print solutions to function
for i in range(n):
    sol.append(np.exp(1j*(2*np.pi*i)/n))
print("Solutions are",*sol,sep="\n")
#fill matrix C with values
for i in range(1000):
    for j in range(1000):
        C[i,j] = x[j] + 1j*y[999-i]
#perform Newton's iterations 20 times to matrix C 
for i in range(20):
    C = C - (((C**n)-1)/(n*(C)**(n-1)))
#fill integer matrix with color values
for i in range(1000):
    for j in range(1000):
        for m in range(n):
            minimum.append(abs(C[i,j]-sol[m])/abs(sol[m])) #check to see which root solution error is smallest compared to this value
        int_matrix[i,j] = (np.argmin(minimum))*255/(n-1) #assign color values to each root and store in a list to graph
        minimum.clear()
#graph color integer matrix
plt.imshow(int_matrix,cmap = "rainbow",origin = "upper",interpolation = "bilinear",extent = (xmin,xmax,ymin,ymax))
plt.xlabel("x")
plt.ylabel("y")
plt.show()
            
