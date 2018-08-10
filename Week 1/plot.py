#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 20:11:05 2018

@author: Edward
"""

import numpy as np
import pylab as plt

#Matrix
X = np.array([[1, 2, 3], [4, 5, 6]])
Y= np.array([[2, 4, 6], [8, 10, 12]])
print(X[:,1]) #col
print(X[1]) #row
#plot
#plt.plot([0,1,2],[0,1,4],"rd-")

#log equally spaced plot
#x=np.logspace(0,1,10) 
#y=x**2 
#plt.subplot(211)
#plt.loglog(x,y,"bo-")
#plt.subplot(212, facecolor='y')
# now create a subplot which represents the top plot of a grid
# with 2 rows and 1 column. Since this subplot will overlap the
# first, the plot (and its axes) previously created, will be removed

#histogram
x = np.random.normal(size=1000)
plt.hist(x, normed = True, bins = np.linspace(-5, 5, 21))

y = np.random.gamma(2, 3, 100000)
plt.hist(x, bins = 30, cumulative = True, normed = True, histtype = "step")
