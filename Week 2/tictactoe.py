#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 19:19:09 2018

@author: Edward
"""

import numpy as np

def create_board():
    return np.zeros((3, 3))

def place(board, player, position):
    rightPlayer = True
    while rightPlayer:
        if board[position] == 0:
            board[position] = player
            rightPlayer = False

def possibilities(board):
    return board[np.where(board == 0)]

board = create_board()
place(board, 1, (0,0))
possibilities(board)
