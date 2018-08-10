#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 21:24:32 2018

@author: Edward
"""

#pwd #directory
#cd  #Change directory

inputfile = "dna.txt"
f = open(inputfile, "r")
seq = f.read()
seq = seq.replace("\n", "")
seq = seq.replace("\r", "") #may not be visible