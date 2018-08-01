#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 08:54:38 2018

@author: Edward
"""

import random

random.seed(1)

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    mean_values=[]
    for i in range(1,n+1):
        mean_values.append((x[i-1] + x[i] + x[i+1])/width)
    return (mean_values)

x=[0,10,5,3,1,5]
print(moving_window_average(x, 1))

R = 1000
x = []
Y= []
for i in range(R):
    num = random.uniform(0,1)
    x.append(num)
Y.append(x)

for i in range(1,10):
    mov_avg = moving_window_average(x, n_neighbors=i)
    Y.append(mov_avg) 

ranges = [max(L) - min(L) for L in Y]
print(ranges)