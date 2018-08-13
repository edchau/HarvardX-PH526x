#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 16:47:50 2018

@author: Edward
"""

#Intro to Statistical Learning
#Supervised Learning: Input -> Output
#Unsupervised Learning: Input
#Quantitative: Regression Problem
#Qualitative: Classification Problem
#Loss function: which is a way of quantifying how far our 
#predictions for Y for a given value of X are from the true 
#observed values of Y. 

#First, in a regression setting, by far the most common loss function
#is the so-called squared error loss.
#the best value to predict for a given X
#is a conditional expectation, or a conditional average,
#of Y given X. 
#So what that means is that what we should predict
#is the average of all values of Y that correspond to a given value of X.

#Second, in a classification setting, we most often
#use the so-called 0-1 loss function, and in that case,=
#the best classification for a given X is obtained
#by classifying observation of the class with the highest
#conditional probability given X. In other words, for a given value of X,
#we compute the probability of each class and we then
#assign the observation to the class with the highest probability.


#Generating Regression Data
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

n = 100
beta_0 = 5
beta_1 = 2
np.random.seed(1)
x = 10 * ss.uniform.rvs(size=n) #0-1 interval
y = beta_0 + beta_1 * x + ss.norm.rvs(loc=0, scale=1, size=n)

plt.figure()
plt.plot(x,y,"o",ms=5)
xx = np.array([0,10])
plt.plot(xx, beta_0 + beta_1 * xx)
plt.xlabel("x")
plt.ylabel("y")


#Least Squares Estimation
rss = []
slopes = np.arange(-10, 15, 0.01)
for slope in slopes:
    rss.append(np.sum((y - beta_0 - slope * x) ** 2))
ind_min = np.argmin(rss)
print("Estimate for the slope: ", slopes[ind_min])

#Plot figure
plt.figure()
plt.plot(slopes, rss)
plt.xlabel("Slope")
plt.ylabel("RSS")


#Simple Linear Regression
import statsmodels.api as sm
mod = sm.OLS(y,x) #Ordinary Least Squares (y, predictor)
est = mod.fit()
print(est.summary()) #slope of line higher than true slope bc starts at origin

X = sm.add_constant(x)
mod = sm.OLS(y, X)
est = mod.fit()
print(est.summary()) #closer to true value 2.0

#1.9685 (slope est) +- 1.96 * 0.031 (standard error) -> 95% confidence interval
#RSS is defined as the sum of the squared differences between the outcome yi
#and the outcome predicted by the model yi hat.


#Multiple Linear Regression
#the goal is to predict a quantitative or a scalar valued
#response, Y, on the basis of several predictor variables.


#scikit-learn for linear regression
n = 500
beta_0 = 5
beta_1 = 2
beta_2 = -1
np.random.seed(1)
x_1 = 10 * ss.uniform.rvs(size=n)
x_2 = 10 * ss.uniform.rvs(size=n)
y = beta_0 + beta_1 * x_1 + beta_2 * x_2 + ss.norm.rvs(loc=0, scale=1, size=n)

X = np.stack([x_1, x_2], axis=1)

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], y, c=y)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_zlabel("$y$");


from sklearn.linear_model import LinearRegression
lm = LinearRegression(fit_intercept=True) #nonzero intercept in data
lm.fit(X,y)
lm.intercept_
lm.coef_[0] #Beta 1
lm.coef_[1] #Beta 2
X_0 = np.array([2, 4])
lm.predict(X_0.reshape(1,-1)) #reshape based on warning
lm.score(X, y) #generates prediction y^  based on input X
#R^2 values .98, really high


#Assessing Model Accuracy
from sklearn.model_selection import train_test_split
#split dataset into training data and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, random_state = 1)
#X predictors, y outcomes
lm = LinearRegression(fit_intercept=True)
lm.fit(X_train, y_train)
lm.score(X_test, y_test)
#predictors, true values
#high R^2 value, more accurate