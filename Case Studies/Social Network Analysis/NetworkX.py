#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 13:36:18 2018

@author: Edward
"""

import networkx as nx


#Basics of NetworkX
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(["u","v"])
print(G.nodes())

G.add_edge(1,2)
G.add_edge("u","v")
G.add_edges_from([(1,3),(1,4),(1,4),(1,6)])
G.add_edge("u","w")
print(G.edges())

G.remove_node(2)
G.remove_nodes_from([4,5])
print(G.nodes())

G.remove_edge(1,3)
G.remove_edges_from([(1,2), ("u","v")])
print(G.edges)

print(G.number_of_nodes())
print(G.number_of_edges())


#Graph Visualization
import matplotlib.pyplot as plt
G = nx.karate_club_graph()
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
plt.savefig("karate_graph.pdf")
print(G.degree())
print(G.degree()[33])
print(G.degree(33))


#Erdős-Rényi graph
#N:number of nodes
#p:probability of connection
from scipy.stats import bernoulli
bernoulli.rvs(p=0.2) #mostly 0's, occasionally 1's
N = 20
p = 0.2

#Create empty graph
#add all N nodes in the graph
#loop over all pairs of nodes
    #add edge with prob p

#n = 10, p = 0: 10 components
# n = 10, p = 1: 1 component
def er_graph(N, p):
    """
    Generate an ER graph
    """
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p): #p=0.2, 1 is True
                G.add_edge(node1, node2)
    return G

nx.draw(er_graph(50, 0.08), node_size=40, node_color="gray")
plt.savefig("er1.pdf")


#Plotting Degree Distribution
def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree Distribution")

G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)
G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)
G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)

plt.savefig("hist3.pdf")


#Descriptive Statistics of Empirical Solutions
import numpy as np
A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

def basic_net_stats(G):
    print("Number of nodes: %d", G.number_of_nodes())
    print("Number of edges: %d", G.number_of_edges())
    degree_sequence = [d for n, d in G.degree()]
    print("Average degree: %.2f" % np.mean(degree_sequence))

basic_net_stats(G1)
basic_net_stats(G2)

plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.savefig("village_hist.pdf") #not a lot of people have large number of connections


#Largest Connected Component
gen = nx.connected_component_subgraphs(G1)
#g = gen.__next__()
#g.number_of_nodes()
#len(gen.__next__()) #next subsequent component
#len(G1) == G1.number_of_nodes()

#Computes largest connected component
G1_LCC = max(nx.connected_component_subgraphs(G1), key=len)
G2_LCC = max(nx.connected_component_subgraphs(G2), key=len)

print(G1_LCC.number_of_nodes() / G1.number_of_nodes())
#97% of nodes in G1 contained in largest component
print(G2_LCC.number_of_nodes() / G2.number_of_nodes())
#92% of nodes in G2 contained in largest component

plt.figure()
nx.draw(G1_LCC, node_color="red", edge_color="gray", node_size=20)
plt.savefig("village1.pdf")

plt.figure()
nx.draw(G2_LCC, node_color="green", edge_color="gray", node_size=20)
plt.savefig("village2.pdf")
#algorithm is stochastic: different trials result in different results
#largest component of G2 in 2 separate groups
#a community is a group of nodes that are densely 
#connected to other nodes in the group,
#but only sparsely connected nodes outside of that group.
