#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:48:52 2018

@author: Edward
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Loading and Inspecting Data
whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")

print(whisky.iloc[5:10, 0:5])
#print(whisky.columns)

flavors = whisky.iloc[:, 2:14]
print(flavors)


#Exploring Correlations
corr_flavors = pd.DataFrame.corr(flavors)
#print(corr_flavors)

plt.figure(figsize = (10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")


corr_whisky = pd.DataFrame.corr(flavors.T)

plt.figure(figsize = (10,10))
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.savefig("corr_whisky.pdf")


#Spectral co-clustering to cluster whiskies based on flavor profiles
from sklearn.cluster.bicluster import SpectralCoclustering

#spectral: eigenvalues/eigenvectors
model = SpectralCoclustering(n_clusters = 6, random_state = 0)
model.fit(corr_whisky)
print(model.rows_)
print(np.sum(model.rows_, axis = 1))
print(np.sum(model.rows_, axis = 0)) #1's
print(model.row_labels_) #observation index belongs to cluster 0-5


#Comparing Correlation Matrices
#Rename indices to match sorting
#Append group labels from model to whisky table
whisky['Group'] = pd.Series(model.row_labels_, index = whisky.index)
#Reorder rows by increasing group order from spectral coclustering
whisky = whisky.ix[np.argsort(model.row_labels_)] #changes appearance but leaves indices same
#Reset index of dataframe
whisky = whisky.reset_index(drop = True) #resets indices in increasing order

correlations = pd.DataFrame.corr(whisky.iloc[:, 2:14].T)
correlations = np.rray(correlations)

plt.figure(figsize = (14, 7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")
plt.savefig("correlations.pdf")
#see 6 blocks of whiskies along line , similar flavors
