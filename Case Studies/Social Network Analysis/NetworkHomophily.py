#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 15:47:08 2018

@author: Edward
"""

#Case Study 6 - Network Homophily
#Network homophily occurs when nodes that share an edge share a 
#characteristic more often than nodes that do not share an edge.

#Exercise 1
#In this exercise, we will calculate the chance homophily for an 
#arbitrary characteristic. Homophily is the proportion of edges in
#the network whose constituent nodes share that characteristic. 
#How much homophily do we expect by chance? If characteristics are 
#distributed completely randomly, the probability that two nodes x 
#and y share characteristic a is the probability both nodes have 
#characteristic a, which is the frequency of a squared. The total 
#probability that nodes x and y share their characteristic is therefore 
#the sum of the frequency of each characteristic in the network. 
#For example, in the dictionary favorite_colors provided, 
#the frequency of red and blue is 1/3 and 2/3 respectively, 
#so the chance homophily is (1/3)^2+(2/3)^2 = 5/9.

from collections import Counter
def frequency(chars):
    count = Counter(chars.values())
    return count
    
def chance_homophily(chars):
    count = frequency(chars)
    probability = 0
    for freq in count.values():
        probability += (freq / len(chars)) ** 2
    return probability        


favorite_colors = {
    "ankit":  "red",
    "xiaoyu": "blue",
    "mary":   "blue"
}

color_homophily = chance_homophily(favorite_colors)
print(color_homophily)


#Exercise 2
#Subset the data into individual villages and store them

import pandas as pd
#individual_characteristics.dta contains several characteristics 
#for each individual in the dataset such as age, religion, and caste
df  = pd.read_stata(data_filepath + "individual_characteristics.dta")
df1 = df[(df.village == 1)]
df2 = df[(df.village == 2)]

print(df1.head())


#Exercise 3
#Define a few dictionaries that enable us to look up the sex, 
#caste, and religion of members of each village by personal ID. 
#For Villages 1 and 2, their personal IDs are stored as pid.

sex1      = dict(zip(df1.pid, df1.resp_gend))
caste1    = dict(zip(df1.pid, df1.caste))
religion1 = dict(zip(df1.pid, df1.religion))

sex2      = dict(zip(df2.pid, df2.resp_gend))
caste2    = dict(zip(df2.pid, df2.caste))
religion2 = dict(zip(df2.pid, df2.religion))


#Exerise 4
#print the chance homophily of several characteristics of Villages 
#1 and 2.

print("Village 1 chance of same sex:", chance_homophily(sex1))
print("Village 1 chance of same caste:", chance_homophily(caste1))
print("Village 1 chance of same religion:", chance_homophily(religion1))

print("Village 2 chance of same sex:", chance_homophily(sex2))
print("Village 2 chance of same caste:", chance_homophily(caste2))
print("Village 2 chance of same religion:", chance_homophily(religion2))


#Exercise 5
#Create a function that computes the observed homophily 
#given a village and characteristic.

def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties = 0
    num_ties = 0
    for n1, n2 in G.edges():
        if IDs[n1] in chars and IDs[n2] in chars:
            if G.has_edge(n1, n2):
                num_ties += 1
                if chars[IDs[n1]] == chars[IDs[n2]]:
                    num_same_ties += 1
    return (num_same_ties / num_ties)    
    

#Exercise 6
#Obtain the personal IDs for Villages 1 and 2
#In this dataset, each individual has a personal ID, or PID, stored 
#in key_vilno_1.csv and key_vilno_2.csv for villages 1 and 2, respectively. 
#data_filepath contains the base URL to the datasets used in this exercise

pid1 = pd.read_csv(data_filepath + "key_vilno_1.csv", header=None)
pid2 = pd.read_csv(data_filepath + "key_vilno_2.csv", header=None)


#Exercise 7
#Compute the homophily of several network characteristics for Villages 1 and 
#2, and compare this to chance homophily. The networks for these villages 
#have been stored as networkx graph objects G1 and G2. homophily() and 
#chance_homophily() are pre-loaded from previous exercises.

import networkx as nx
G1 = nx.Graph()
G2 = nx.Graph()

print("Village 1 observed proportion of same sex:", homophily(G1, sex1, pid1))
print("Village 1 observed proportion of same caste:", homophily(G1, religion1, pid1))
print("Village 1 observed proportion of same religion:", homophily(G1, caste1, pid1))

print("Village 2 observed proportion of same sex:", homophily(G2, sex2, pid2))
print("Village 2 observed proportion of same caste:", homophily(G2, caste2, pid2))
print("Village 2 observed proportion of same religion:", homophily(G2, religion2, pid2))

print("Village 1 chance proportion of same sex:", chance_homophily(sex1))
print("Village 1 chance proportion of same caste:", chance_homophily(caste1))
print("Village 1 chance proportion of same religion:", chance_homophily(religion1))

print("Village 2 chance proportion of same sex:", chance_homophily(sex1))
print("Village 2 chance proportion of same caste:", chance_homophily(caste1))
print("Village 2 chance proportion of same religion:", chance_homophily(religion1))



