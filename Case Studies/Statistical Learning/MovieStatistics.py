#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 13:55:32 2018

@author: Edward
"""

#Case Study 7: Movie Revenue Prediction Part 1
#The movie dataset on which this case study is based is a database of 5000 
#movies catalogued by The Movie Database (TMDb). The information available 
#about each movie is its budget, revenue, rating, actors and actresses, etc. 
#In this case study, we will use this dataset to determine whether any 
#information about a movie can predict the total revenue of a movie. 
#We will also attempt to predict whether a movie's revenue will exceed its budget


#Exercise 1
#import several libraries. scikit-learn (sklearn) contains helpful 
#statistical models, and we'll use the matplotlib.pyplot library 
#for visualizations. Of course, we will use numpy and pandas for 
#data manipulation throughout.
import pandas as pd
import numpy as np

from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt

df = pd.read_csv(data_filepath + 'merged_movie_data.csv')
print(df.head())


#Exercise 2
#we will define the regression and classification outcomes. Specifically, 
#we will use the revenue column as the target for regression. For 
#classification, we will construct an indicator of profitability for each movie.
df.loc[df["revenue"] >  df["budget"],"profitable"] = 1
df.loc[df["revenue"] <=  df["budget"],"profitable"] = 0
df["profitable"] = pd.to_numeric(df["profitable"]).astype(int)
regression_target = "revenue"
classification_target = "profitable"


#Exercise 3
#For simplicity, we will proceed by analyzing only the rows without any 
#missing data. In this exercise, we will remove rows with any infinite 
#or missing values.
df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna()


#Exercise 4
#Many of the variables in our dataframe contain the names of genre, 
#actors/actresses, and keywords. Let's add indicator columns for each genre.
genres_list = df.genres.apply(lambda x: x.split(","))
genres = []
for row in genres_list:
    row = [genre.strip() for genre in row]
    for genre in row:
        if genre not in genres:
            genres.append(genre)

for genre in genres:
    df[genre] = df['genres'].str.contains(genre).astype(int)

print(df[genres].head())


#Exercise 5
#we will store the names of these variables for future use. We will also 
#take a look at some of the continuous variables and outcomes by plotting 
#each pair in a scatter plot. Finally, we will evaluate the skew of each variable.
continuous_covariates = ['budget', 'popularity', 'runtime', 'vote_count', 'vote_average']
outcomes_and_continuous_covariates = continuous_covariates + [regression_target, classification_target]
plotting_variables = ['budget', 'popularity', regression_target]

axes = pd.tools.plotting.scatter_matrix(df[plotting_variables], alpha = 0.15,color=(0,0,0),hist_kwds={"color":(0,0,0)},facecolor=(1,0,0))
plt.tight_layout()
plt.show()
df[outcomes_and_continuous_covariates].skew()


#Exercise 6
#It appears that the variables budget, popularity, runtime, vote_count, and 
#revenue are all right-skewed. In this exercise, we will transform these 
#variables to eliminate this skewness. Specifically, we will use the np.log10()
#method. Because some of these variable values are exactly 0, we will add a 
#small positive value to each to ensure it is defined. (Note that for any base, 
#log(0) is negative infinity!)
df.budget = np.log10(1+df.budget)
df.popularity = np.log10(1+df.popularity)
df.runtime = np.log10(1+df.runtime)
df.vote_count = np.log10(1+df.vote_count)
df.revenue = np.log10(1+df.revenue)



#Case Study 7: Movie Revenue Prediction Part 2
#In Part 2 of this case study, we will primarily use the two models we 
#recently discussed: linear/logistic regression and random forests to 
#perform prediction and classification. We will use these methods to 
#predict revenue, and logistic regression to classify whether a movie 
#was profitable.

#Exercise 1
#We will instantiate regression and classification models. Code is 
#provided that prepares the covariates and outcomes we will use for 
#data analysis.
# Define all covariates and outcomes from `df`.
regression_outcome = df[regression_target]
classification_outcome = df[classification_target]
covariates = df[all_covariates]

# Instantiate all regression models and classifiers.
linear_regression = LinearRegression()
logistic_regression = LogisticRegression()
forest_regression = RandomForestRegressor(max_depth=4,random_state=0)
forest_classifier = RandomForestClassifier(max_depth=4,random_state=0)


#Exercise 2
#we will create two functions that compute a model's score. For regression 
#models, we will use correlation as the score. For classification models, 
#we will use accuracy as the score.

def correlation(estimator, X, y):
    linear_regression.fit(X,y)
    linear_regression.predict(estimator.reshape(1,-1))
    return linear_regression.r2_score(X,y)

def accuracy(estimator, X, y):
    linear_regression.fit(X,y)
    linear_regression.predict(estimator.reshape(1,-1))
    return linear_regression.accuracy_score(X,y)


#Exercise 3
#we will compute the cross-validated performance for the linear and 
#random forest regression models.

# Determine the cross-validated correlation for linear and random forest models.
linear_regression_scores = cross_val_score(linear_regression, covariates, regression_outcome, cv=10, scoring=correlation)
forest_regression_scores = cross_val_score(forest_regression, covariates, regression_outcome,cv=10, scoring=correlation)

# Plot Results
plt.axes().set_aspect('equal', 'box')
plt.scatter(linear_regression_scores, forest_regression_scores)
plt.plot((0, 1), (0, 1), 'k-')

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("Linear Regression Score")
plt.ylabel("Forest Regression Score")

# Show the plot.
plt.show()


#Exercise 4
#we will compute the cross-validated performance for the linear and random 
#forest classification models.
# Determine the cross-validated accuracy for logistic and random forest models.
logistic_regression_scores = cross_val_score(logistic_regression, covariates, classification_outcome, cv=10, scoring=accuracy)
forest_classification_scores = cross_val_score(forest_classifier, covariates, classification_outcome,cv=10, scoring=accuracy)
# Plot Results
plt.axes().set_aspect('equal', 'box')
plt.scatter(logistic_regression_scores, forest_classification_scores)
plt.plot((0, 1), (0, 1), 'k-')

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("Linear Classification Score")
plt.ylabel("Forest Classification Score")

# Show the plot.
plt.show()


#Exercise 5
#we will exclude these movies, and rerun the analyses to determine if the 
#fits improve. In this exercise, we will rerun the regression analysis 
#for this subsetted dataset.
positive_revenue_df = df.loc[df["revenue"] > 0]
# Replace the dataframe in the following code, and run.

regression_outcome = positive_revenue_df[regression_target]
classification_outcome = positive_revenue_df[classification_target]
covariates = positive_revenue_df[all_covariates]

# Reinstantiate all regression models and classifiers.
linear_regression = LinearRegression()
logistic_regression = LogisticRegression()
forest_regression = RandomForestRegressor(max_depth=4, random_state=0)
forest_classifier = RandomForestClassifier(max_depth=4, random_state=0)
linear_regression_scores = cross_val_score(linear_regression, covariates, regression_outcome, cv=10, scoring=correlation)
forest_regression_scores = cross_val_score(forest_regression, covariates, regression_outcome, cv=10, scoring=correlation)
logistic_regression_scores = cross_val_score(logistic_regression, covariates, classification_outcome, cv=10, scoring=accuracy)
forest_classification_scores = cross_val_score(forest_classifier, covariates, classification_outcome, cv=10, scoring=accuracy)


#Exercise 6
#we will compute the cross-validated performance for the linear and random 
#forest regression models for positive revenue movies only.
# Determine the cross-validated correlation for linear and random forest models.
# Determine the cross-validated correlation for linear and random forest models.
linear_regression_scores = cross_val_score(linear_regression, covariates, regression_outcome, cv=10, scoring=correlation)
forest_regression_scores = cross_val_score(forest_regression, covariates, regression_outcome,cv=10, scoring=correlation)


# Plot Results
plt.axes().set_aspect('equal', 'box')
plt.scatter(linear_regression_scores, forest_regression_scores)
plt.plot((0, 1), (0, 1), 'k-')

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("Linear Regression Score")
plt.ylabel("Forest Regression Score")

# Show the plot.
plt.show()
# Print the importance of each covariate in the random forest regression.
forest_classifier.fit(positive_revenue_df[all_covariates], classification_outcome)
for row in zip(all_covariates, forest_classifier.feature_importances_,):
        print(row)


#Exercise 7
logistic_regression_scores = cross_val_score(logistic_regression, covariates, classification_outcome, cv=10, scoring=accuracy)
forest_classification_scores = cross_val_score(forest_classifier, covariates, classification_outcome,cv=10, scoring=accuracy)

# Plot Results
plt.axes().set_aspect('equal', 'box')
plt.scatter(logistic_regression_scores, forest_classification_scores)
plt.plot((0, 1), (0, 1), 'k-')

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("Linear Classification Score")
plt.ylabel("Forest Classification Score")

# Show the plot.
plt.show()
# Print the importance of each covariate in the random forest classification.
forest_classifier.fit(positive_revenue_df[all_covariates], classification_outcome)
for row in zip(all_covariates, forest_classifier.feature_importances_,):
        print(row)

