#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 08:47:02 2018

@author: Edward
"""

import string

alphabet = string.ascii_letters
sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}

for letter in sentence:
    if letter not in alphabet:
        continue
    if letter not in count_letters:
        count_letters[letter] = 1
    else:
        count_letters[letter] += 1
        
def counter(input_string):
    count_letters = {}
    for letter in input_string:
        if letter not in string.ascii_letters:
            continue
        if letter not in count_letters:
            count_letters[letter] = 1
        else:
            count_letters[letter] += 1
    return count_letters

address_count = counter(sentence)
print(address_count)
most_frequent_letter = ""
maximum = max(address_count.values())

for letter in address_count:
    if address_count[letter] == maximum:
        most_frequent_letter = letter 
print(most_frequent_letter)
