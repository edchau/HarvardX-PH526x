#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 13:50:54 2018

@author: Edward
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

birddata =  pd.read_csv("bird_tracking.csv")
print(birddata.info())
print(birddata.head())


#Simple Data Visualization
ix = birddata.bird_name == "Eric"
x,y = birddata.longitude[ix], birddata.latitude[ix]
plt.figure(figsize = (7,7))
plt.plot(x,y, ".") #Flight Trajectory for Eric

bird_names = pd.unique(birddata.bird_name)
plt.figure(figsize = (7,7))
for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x,y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x,y, ".", label=bird_name) #Flight Trajectory
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.savefig("3traj.pdf")
    

#Examining Flight Speed
plt.figure('Speed')
ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]
#plt.hist(speed) #return errors
#print(np.isnan(speed).any()) #True: at least 1 NaN
#print.sum(np.isnan(speed)) #85 entires not numeric
ind = np.isnan(speed)
plt.hist(speed[~ind]) #~ not equal

plt.figure(figsize=(8,4))
speed = birddata.speed_2d[birddata.bird_name == "Eric"]
ind = np.isnan(speed)
plt.hist(speed[~ind], bins = np.linspace(0, 30, 20), normed = True) #normed: integral of hist = 1
plt.xlabel("2D Speed (m/s)")
plt.ylabel("Frequency"); 
plt.savefig("hist.pdf")
#Speed of Eric


#Using Pandas: don't have to deal w/ NaN's
birddata.speed_2d.plot(kind='hist', range=[0,30])
plt.xlabel("2D Speed")
plt.savefig("pd_hist.pdf")


#Using Datetime
print(birddata.date_time[0:3])
time_1 = datetime.datetime.today() #current day and time stamp
time_2 = datetime.datetime.today()
print(time_2-time_1) #time delta object: time elapsed

timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime\
    (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))
    #ignores UTC

birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)
print(birddata.timestamp[4] - birddata.timestamp[3])

#Amount of Time Elapsed since beginning of Data Collection
times = birddata.timestamp[birddata.bird_name == "Eric"]
elapsed_time = [time - times[0] for time in times] 
#How many days have passed:
print(elapsed_time[1000] / datetime.timedelta(days = 1))
#How many hours have passed
print(elapsed_time[1000] / datetime.timedelta(hours = 1))


plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1))
plt.xlabel("Observation")
plt.ylabel("Elapsed Time (Days)");
plt.savefig("timeplot.pdf")


#Calculating Daily Mean Speed
data = birddata[birddata.bird_name == "Eric"]
times = data.timestamp
elapsed_time = [time - times[0] for time in times] 
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []

for (i,t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        #compute mean speed
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []
    
plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean Speed (m/s)");
plt.savefig("dms.pdf")


#Using the Cartopy Library
import cartopy.crs as ccrs
import cartopy.feature as cfeature

#standard projection
proj = ccrs.Mercator()

plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle = ':')

for name in bird_names:
    ix = birddata['bird_name'] == name
    x,y = birddata.longitude[ix], birddata.latitude[ix]
    ax.plot(x,y,'.',transform=ccrs.Geodetic(),label=name)
    #projected trajectories
plt.legend(loc="upper left")
plt.savefig("map.pdf")