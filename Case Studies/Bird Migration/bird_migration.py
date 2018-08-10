#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 16:52:30 2018

@author: Edward
"""

#Case Study 5 - Bird Migration

import pandas as pd
import datetime
import matplotlib.pyplot as plt

birddata =  pd.read_csv("bird_tracking.csv") #load dataframe

#Exercise 1
#Group the dataframe by birdname and then find the average speed_2d for each bird

grouped_birds = birddata.groupby('bird_name')

#Mean of `speed_2d` using the `mean()` function.
mean_speeds = grouped_birds['speed_2d'].mean()

print(grouped_birds.head())

# Find the mean `altitude` for each bird.
mean_altitudes = grouped_birds['altitude'].mean()


#Exercise 2
#Group the flight times by date and calculate the mean altitude within that day

# Convert birddata.date_time to the `pd.datetime` format.
birddata.date_time = pd.to_datetime(birddata['date_time'])

# Create a new column of day of observation
birddata['date'] = birddata['date_time'].dt.date

# Check the head of the column.
print(birddata.date.head())

# Use `groupby()` to group the data by date.
grouped_bydates = birddata.groupby('date')

# Find the mean `altitude` for each date.
mean_altitudes_perday = grouped_bydates['altitude'].mean()


#Exercise 3
#Group the flight times by both bird and date, and calculate 
#the mean altitude for each.

# Use `groupby()` to group the data by bird and date.
grouped_birdday = birddata.groupby(["bird_name", "date"])

# Find the mean `altitude` for each bird and date.
mean_altitudes_perday = grouped_birdday['altitude'].mean()

print(mean_altitudes_perday.head())


#Exercise 4
#Find the average speed for each bird and day.
eric_daily_speed  = grouped_birdday['speed_2d'].mean()["Eric"]
sanne_daily_speed = grouped_birdday['speed_2d'].mean()["Sanne"]
nico_daily_speed  = grouped_birdday['speed_2d'].mean()["Nico"]

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.xticks(10)
plt.show()
