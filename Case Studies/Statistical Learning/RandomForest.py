#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 13:16:32 2018

@author: Edward
"""

#Random Forest for regression and classification
#Considers predictions of several trees, randomized trees
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
#Regression: mean of predictions of individual trees
#Classification: mode of predictions of individual trees
#Each time we make a split, we take a new sample of predictors.

