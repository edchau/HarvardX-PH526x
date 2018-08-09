#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 17:19:50 2018

@author: Edward
"""

#Case Study 3: Wine Classification 

#In this case study, we will analyze a dataset consisting of an assortment of 
#wines classified as "high quality" and "low quality" and will use the k-Nearest 
#Neighbors classifier to determine whether or not other information about the wine 
#helps us correctly predict whether a new wine will be of high quality.

def distance(p1, p2):
    """
    Find the distance between points
    p1 and p2
    """
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def majority_vote(votes):
    """
    Returns most common element in votes (Random if tie)
    """
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
            
    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)    
            
    return random.choice(winners) #if tie, return random winner

def find_nearest_neighbors(p, points, k = 5):
    """
    Find the k nearest neighbors of point p and
    return their indices
    """
    distances = np.zeros(points.shape[0]) 
    for i in range(len(distances)):
        distances[i] = distance(p, points[i]) #distances from point p
    ind = np.argsort(distances) #list of indices
    return ind[:k]

def knn_predict(p, points, outcomes, k = 5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])



#Exercise 1
#Read data from link and store in dataframe

import pandas as pd
data = pd.read_csv("https://s3.amazonaws.com/demo-datasets/wine.csv")


#Exercise 2
#Drop color column from data set b/c redundancy 

print(data.head(5))
numeric_data = data.drop('color', axis=1)


#Exercise 3
#Scale the numeric data and extract the first two principal components.
#Scale the data by subtracting the mean of each column and 
#dividing each column by its standard deviation
#Use principal components to take a linear snapshot of the 
#data from several different angles
import sklearn.preprocessing
scaled_data = sklearn.preprocessing.scale(numeric_data)
numeric_data = pd.DataFrame(scaled_data, columns =numeric_data.columns)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit_transform(numeric_data)


#Exercise 4
#Plot the first two principal components of the covariates in the dataset
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:,0]
y = principal_components[:,1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2,
    c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1"); plt.ylabel("Principal Component 2")
plt.show()


#Exercise 5
import numpy as np

def accuracy(predictions, outcomes): 
    """
    Takes two lists of the same size as arguments.
    Returns a single number, which is the percentage of 
    elements that are equal for the two lists.
    """
    100 * np.mean(predictions == outcomes)

x = np.array([1,2,3])
y = np.array([1,2,4])
print(accuracy(x, y))


#Exercise 6
#Calculate low quality wines
print(accuracy(0, data["high_quality"]))


#Exercise 7
#Predict quality of wines in dataset
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, data['high_quality'])
library_predictions = knn.predict(numeric_data)
print(accuracy(library_predictions, data["high_quality"]))
#Prediction results in much more accuracy than Exercise 6


#Exercise 8
#Select a subset of data to use in homemade kNN classifier.
import random
n_rows = data.shape[0]
random.seed(123)
selection = random.sample(range(n_rows), 10)

#Exercise 9
#Use homemade kNN classifier to compare accuracy of results to baseline
predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(data["high_quality"])

my_predictions = [knn_predict(p, predictors[training_indices,:], outcomes, k=5) for p in predictors[selection]]
percentage = accuracy(my_predictions, data.high_quality[selection])

print(percentage)
