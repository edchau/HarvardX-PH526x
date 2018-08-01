#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 08:51:34 2018

@author: Edward
"""

import math
import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

print(math.pi/4)

def rand():
    random.uniform(-1, 1)
rand()

def distance(x, y):
   return math.sqrt((y[0]-x[0]) + (y[1]-x[1]))
   
print(distance((0,0), (1,1)))

def in_circle(x, origin = [0]*2):
   if (x[0] - origin[0]) < 1:
       return True
   else:
       return False


R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    if in_circle(point):
        inside.append(True)
    else:
        inside.append(False)

print(inside.count(True) / R - math.pi/4)