#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 22:17:04 2018

@author: Edward
"""

import string

#Case Study 1 - Caesar Cipher

#Exercise 1
#String with lowercase letters
alphabet = ' ' + string.ascii_lowercase

#Exercise 2
#Create Dictionary with key as letter and value as corresponding number
positions = {alphabet[i]:i for i in range(0,27)}

#Exercise 3 and 4
#Create encoded message
message = "hi my name is caesar"

def encoding(message, key):
    """
    returns encoded message shifted by key as a single string
    """
    encoder = {alphabet[i]:((i + key) % 27) for i in range(27)}
    print(encoder)
    return ''.join([alphabet[encoder[letter]] for letter in message])

encoded_message = encoding(message, 1)
print(encoded_message)

#Exercise 5
#Decode message with negative key
decoded_message = encoding(encoded_message, -1)
print(decoded_message)