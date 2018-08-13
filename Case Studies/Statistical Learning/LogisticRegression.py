#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 22:27:04 2018

@author: Edward
"""

#Generate and plot classification data
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
#%matplotlib notebook

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

np.random.seed(1)
h = 1
sd = 1
n = 50

def gen_data(n, h, sd1, sd2):
    x1 = ss.norm.rvs(-h, sd1, n) #class 1, blue
    y1 = ss.norm.rvs(0, sd1, n)
    x2 = ss.norm.rvs(h, sd2, n) #class 2, orange
    y2 = ss.norm.rvs(0, sd2, n) #bigger bc greater std deviation
    
    return (x1, y1, x2, y2)

(x1, y1, x2, y2) = gen_data(50, 1, 1, 1.5)
(x1, y1, x2, y2) = gen_data(1000, 1.5, 1, 1.5)

def plot_data(x1, y1, x2, y2):
    plt.figure()
    plt.plot(x1, y1, "o", ms=2)
    plt.plot(x2, y2, "o", ms=2)
    plt.xlabel("$X_1$")
    plt.ylabel("$X_2$")
    
plot_data(x1, y1, x2, y2)


#Logistic Regression
#binary classifierx
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
X = np.vstack((np.vstack((x1, y1)).T, np.vstack((x2, y2)).T))
n = 1000
y = np.hstack((np.repeat(1,n), np.repeat(2,n))) #Use shape to check sizes

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, random_state = 1)
clf.fit(X_train, y_train)
clf.score(X_test, y_test)
clf.predict_proba(np.array([-2, 0]).reshape(1,-1)) #.97 class 1, .03 class 2
clf.predict(np.array([-2, 0]).reshape(1,-1)) #given -2, 0 covariates, class 1
#Train points, test (-2, 0) covariates (look on graph) 
#Score for accuracy, Fit to train, Predict classification based on point
#Similar to linear regression


#Computing Predictive Probabilities
def plot_probs(ax, clf, class_no):
    xx1, xx2 = np.meshgrid(np.arange(-5, 5, 0.1), np.arange(-5, 5, 0.1))
    probs = clf.predict_proba(np.stack((xx1.ravel(), xx2.ravel()), axis=1))
    #ravel stacks two vectors
    Z = probs[:,class_no]
    Z = Z.reshape(xx1.shape)
    CS = ax.contourf(xx1, xx2, Z)
    cbar = plt.colorbar(CS)
    plt.xlabel("$X_1$")
    plt.ylabel("$X_2$")

plt.figure(figsize=(5,8))
ax = plt.subplot(211)
plot_probs(ax, clf, 0)
plt.title("Pred. prob for class 1")
ax = plt.subplot(212)
plot_probs(ax, clf, 1)
plt.title("Pred. prob for class 2");
plt.savefig("PredProb.pdf")