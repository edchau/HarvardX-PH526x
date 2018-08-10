#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:10:51 2018

@author: Edward
"""
import pandas as pd
#dataframe: 2D Array, Series: 1D Array
x = pd.Series([6,3,8,6], index = ["q","w","e","r"])
print(x["w"])
print(x[["r", "w"]])
print(x.index)

sorted(x.index) #returns list of indices
x.reindex(sorted(x.index))

y = pd.Series([7,3,5,2], index = ["e","q","r","t"])
print(x+y) #indices not in both appear as NaN

age = {"Tim":29, "Jim":31, "Pam":27, "Sam":35}
x = pd.Series(age)

data = {'name' : ['Tim', 'Jim', 'Pam', 'Sam'],
        'age' : [29, 31, 27, 35],
        'ZIP' : ['02115', '02130', '67700', '00100']}

x = pd.DataFrame(data, columns = ["name", "age", "ZIP"])

print(x["name"])
print(x.name)
