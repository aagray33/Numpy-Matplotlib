# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:17:56 2019

@author: Ashton Gray
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(7)
n = 1000000
#create a million random numbers for x and y
x_axis = np.random.uniform(-1,1,n)
y_axis = np.random.uniform(-1,1,n)
#create lists
inside_circle = []
pi_approx = []
inside_circle_graphx = []
inside_circle_graphy = []
num = np.arange(1,n+1)

#count points inside unit circle
for i in range(n):
    if x_axis[i]**2+y_axis[i]**2 <= 1:
        inside_circle.append(1)
        inside_circle_graphx.append(x_axis[i])
        inside_circle_graphy.append(y_axis[i])
    else:
        inside_circle.append(0)
#add sum of ones to pi approx list at that spot in list
pi_approx.append(inside_circle[0])
for i in range(n):
     pi_approx.append(pi_approx[i]+inside_circle[i])
pi_approx.remove(pi_approx[0])
#turn numbers into pi approximates
for i in range(n):
    pi_approx[i]=pi_approx[i]*(4/num[i])

print("Using 1 samples, pi is "+str(pi_approx[0]))
print("Using 10 samples, pi is "+str(pi_approx[9]))
print("Using 100 samples, pi is "+str(pi_approx[99]))
print("Using 1000 samples, pi is "+str(pi_approx[999]))
print("Using 10000 samples, pi is "+str(pi_approx[9999]))
print("Using 100000 samples, pi is "+str(pi_approx[99999]))
print("Using 1000000 samples, pi is "+str(pi_approx[999999]))
  
#graph each figure
plt.figure(0)
x = np.linspace(0,n,n)
plt.plot(pi_approx)
plt.xscale("log")
plt.xlabel("#samples")
plt.ylabel("pi")

plt.figure(1)
theta=np.linspace(0,2*np.pi,100)
x=np.cos(theta)
y=np.sin(theta)

plt.subplot(2,2,1)
plt.plot(x,y)
plt.plot(inside_circle_graphx[:10],inside_circle_graphy[:10], '.')
plt.xticks([])
plt.yticks([])
plt.title("n=10, pi=%.3f"%pi_approx[9])

plt.subplot(2,2,2)
plt.plot(x,y)
plt.plot(inside_circle_graphx[:100],inside_circle_graphy[:100], '.')
plt.xticks([])
plt.yticks([])
plt.title("n=100, pi=%.3f"%pi_approx[99])

plt.subplot(2,2,3)
plt.plot(x,y)
plt.plot(inside_circle_graphx[:1000],inside_circle_graphy[:1000], '.')
plt.xticks([])
plt.yticks([])
plt.title("n=1000, pi=%.3f"%pi_approx[999])

plt.subplot(2,2,4)
plt.plot(x,y)
plt.plot(inside_circle_graphx[:10000],inside_circle_graphy[:10000], '.')
plt.xticks([])
plt.yticks([])
plt.title("n=10000, pi=%.3f"%pi_approx[9999])
plt.show(0)
plt.show(1)
