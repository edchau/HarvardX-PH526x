#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 20:29:07 2018

@author: Edward
"""

import random
import pylab as plt
import numpy as np
import time

random.choice(["H", "T"]) #H or T

random.choice(range(1, 7)) #Dice

random.choice(random.choice([range(1,7), range(1, 9), range(1, 11)]))

sum(random.choice(range(10)) for i in range(10)) 
#sum of 10 random integers between 0 and 9

#histogram
#rolls = []
#for k in range(10000):
#    rolls.append(random.choice([1,2,3,4,5,6]))
#plt.hist(rolls, bins = np.linspace(0.5, 6.5, 7))

#ys = []
#for rep in range(100):
#    y = 0
#    for k in range(10):
#        x = random.choice([1,2,3,4,5,6])
#        y = y + x
#    ys.append(y)
#plt.hist(ys);


#generate random array
#np.random.random(5) #1D
#
#np.random.random((5,3)) #2D
#
#np.random.normal(0, 1, (2,5)) #2 rows, 5 col

#X = np.random.randint(1, 7, (100000, 10))
#X.shape #dim
#np.sum(X, axis = 0) #sum rows
#np.sum(X, axis = 1) #sum columns, axis = 2 for 3D
#
#Y = np.sum(X, axis = 1)
#plt.hist(Y);


#Time
#start_time = time.clock()
#end_time = time.clock()
#t = end_time - start_time


#Random Walk
delta_X = np.random.normal(0, 1, (2, 100)) #mean 0, std dev 1
#plt.plot(delta_X[0], delta_X[1], "go")

#X = np.cumsum(delta_X, axis = 1) #cumulative sum of columns
X_0 = np.array(([0], [0]))
X = np.concatenate((X_0, np.cumsum(delta_X, axis = 1)), axis = 1)
plt.plot(X[0], X[1], "ro-")
#plt.savefig("rw.pdf")

