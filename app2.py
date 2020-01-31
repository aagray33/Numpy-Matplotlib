# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:06:08 2019

@author: ashto
"""

import numpy as np
import matplotlib.pyplot as plt

#initialize all values
np.random.seed(7)
n=100000
start_x1_y1 = input("Enter (x,y) of point-1, default is (0.5,0.5): ")
start_x2_y2 = input("Enter (x,y) of point-2, default is (3,2.5): ")
start_x3_y3 = input("Enter (x,y) of point-3, default is (1,3): ")
if start_x1_y1 == "":
    x1,y1 = 0.5,0.5
else:
    x1,y1 = map(float, start_x1_y1.split())
if start_x2_y2 == "":
    x2,y2 = 3,2.5
else:
    x2,y2 = map(float, start_x2_y2.split())
if start_x3_y3 == "":
    x3,y3 = 1,3
else:
    x3,y3 = map(float, start_x3_y3.split())
xmin = min(x1,x2,x3)
xmax = max(x1,x2,x3)
ymin = min(y1,y2,y3)
ymax = max(y1,y2,y3)
xtriang_graph = [x1,x2,x3,x1]
ytriang_graph = [y1,y2,y3,y1]
omega_area = (xmax-xmin)*(ymax-ymin)

#create random numbers and lists
x_axis = np.random.uniform(xmin,xmax,n) 
y_axis = np.random.uniform(ymin,ymax,n)
A = np.array([[x1,x2,x3],[y1,y2,y3],[1,1,1]])
list_of_a_values = []
inside_triangle = []
inside_triangle_graphx = []
inside_triangle_graphy = []
area_approx = []
num = np.arange(1,n+1)

#create list of a values by means of linear algebra
for i in range(n):
    xy1_matrix = np.array([x_axis[i],y_axis[i],1])
    a_values = np.linalg.solve(A,xy1_matrix)
    list_of_a_values.append(a_values)
#add to inside_triangle
for i in range(n):
    if np.any(list_of_a_values[i]<0) == True:
        inside_triangle.append(0)
    else:
        inside_triangle.append(1)
        inside_triangle_graphx.append(x_axis[i])
        inside_triangle_graphy.append(y_axis[i])
#create list of summations of previous values for area approximation
area_approx.append(inside_triangle[0]) #append first value to get loop started
for i in range(n):
    area_approx.append(area_approx[i]+inside_triangle[i])
area_approx.remove(area_approx[0]) #remove the appended first value
#multiply the summation by omega/n
for i in range(n):
    area_approx[i]=area_approx[i]*(omega_area/num[i])
    
print("Using 1 samples, area of triangle is "+str(area_approx[0]))
print("Using 10 samples, area of triangle is "+str(area_approx[9]))
print("Using 100 samples, area of triangle is "+str(area_approx[99]))
print("Using 1000 samples, area of triangle is "+str(area_approx[999]))
print("Using 10000 samples, area of triangle is "+str(area_approx[9999]))
print("Using 100000 samples, area of triangle is "+str(area_approx[99999]))

#plot graph of Area-Trangle vs #samples
plt.figure(0)
x = np.linspace(0,n,n)
plt.plot(num,area_approx)
plt.xscale("log")
plt.xlabel("#samples")
plt.ylabel("Area-Triangle")
#plot graph of each filled triangle
plt.figure(1)
plt.subplot(2,2,1)
plt.plot(xtriang_graph,ytriang_graph)
plt.plot(inside_triangle_graphx[:10],inside_triangle_graphy[:10], '.')
plt.xticks([])
plt.yticks([])
plt.title("n=10, area=%.3f"%area_approx[9])

plt.subplot(2,2,2)
plt.plot(xtriang_graph,ytriang_graph)
plt.plot(inside_triangle_graphx[:100],inside_triangle_graphy[:100], '.')
plt.xticks([])
plt.yticks([])
plt.title("n=100, area=%.3f"%area_approx[99])

plt.subplot(2,2,3)
plt.plot(xtriang_graph,ytriang_graph)
plt.plot(inside_triangle_graphx[:1000],inside_triangle_graphy[:1000], '.')
plt.xticks([])
plt.yticks([])
plt.title("n=1000, area=%.3f"%area_approx[999])

plt.subplot(2,2,4)
plt.plot(xtriang_graph,ytriang_graph)
plt.plot(inside_triangle_graphx[:10000],inside_triangle_graphy[:10000], '.')
plt.xticks([])
plt.yticks([])
plt.title("n=10000, area=%.3f"%area_approx[9999])
plt.show(0)
plt.show(1)
