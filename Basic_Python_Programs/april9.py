# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:51:08 2019

@author: Dell
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import random#this is random module from numpy
x=np.linspace(0,5,10)#creates 10 random numbers between 0 and 5(includes both start and end number).
plt.hist(x,color='green')#plots single dimension data #color arg changes color


y=np.array([1,4,4,4,6,6,6,6,8,8,8,8])
plt.hist(y,color='pink',orientation='horizontal')


plt.xticks([1,2,3,4])#creates points on the x axis
plt.yticks([2,4,6])

plt.hist(x, bins= 2)#create classes like 0-2 , 2-4 etc.
plt.clf()#clears previous plots
plt.xlabel('X axis')#puts label in axis
plt.ylabel('y axis')


x=np.random.rand(5)
y=np.random.rand(5)
s1=[10,20,30,400,500]#size of dots
c1=np.random.rand(5)#randomly choose color of dots 
plt.scatter(x,y,s=s1,c=c1)
plt.show()#shows plot at last


plt.xscale('log')#only takes inbuilt function
plt.title("work")
plt.legend(["curve1"])#takes only one element of a list as arg
















"""
plt.pie
"""


labels='python','C','Ruby'







#np.arrange



#april 12









