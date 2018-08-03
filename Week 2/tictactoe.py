#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 19:19:09 2018

@author: Edward
"""

import numpy as np
import random
import time
import pyplot as plt
#Exercise 1
def create_board(): #3x3 board of 0's
    return np.zeros((3, 3))

board = create_board()

#Exercise 2
def place(board, player, position):
    """
    board: nparray
    player: 1 or 2
    position: tuple with coord in 2D array
    """
    rightPlayer = True
    while rightPlayer:
        if board[position] == 0:
            board[position] = player
            rightPlayer = False
            
place(board, 1, (0,0))

#Exercise 3
def possibilities(board):
    """
    returns list of empty indices (0)
    """
    return board[np.where(board == 0)]

#Exercise 4
def random_place(board, player):
    """
    places piece on board randomly
    """
    available = possibilities(board)
    place(board, player, random.choice(available))
    
random_place(board, 2)

#Exercise 5
board = create_board()
for i in range(3):
    for player in [1, 2]:
        random_place(board, player)  
                                                                
print(board)

#Exercise 6

def row_win(board, player):
    """
    determines if any row consists of only their marker
    return True of this condition is met, and False otherwise
    """
    for row in board:
        if check_row(row, player):
            return True
    return False  

def check_row(row, player):
    """
    checks for marker of player in row
    """
    for marker in row:
        if marker != player:
            return False
    return True

row_win(board, 1)

#Exercise 7
def col_win(board, player):
    """
    checks for marker of player in col
    transposes array to switch col and row
    """
    for row in board.T:
        if check_row(row, player):
            return True
    return False

col_win(board, 1)

#Exercise 8
def diag_win(board, player):
    forward = board.diagonal() #forward diagonal
    anti = np.flipud(board).diagonal() #flip board to get forward diagonal
    return check_row(forward, player) or check_row(anti, player)                                    

diag_win(board, 1)

#Exercise 9
def evaluate(board):
    """
    returns winner using row, col, diag checks
    """
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
            
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

evaluate(board)

#Exercise 10
def play_game():
    """
    randomly place pieces until one player wins
    """
    board = create_board()
    while True:
        for player in [1, 2]:
            random_place(board, player)
            result = evaluate(board)
            if result != 0:
                return result             
             
play_game()

#Exercise 11
start_time = time.time()
 
games = 1000 #number of iterations
result = []
for i in range(games):
    result.append(play_game())                

end_time = time.time()

print(end_time - start_time)

plt.hist(result) #histogram of 1000 games
plt.savefig('tictactoe_hist.pdf')
plt.show()

#Result:
"""
Player 1 wins more than Player 2, games sometimes end in draw
total amount of time is a few seconds
"""

#Exercise 12
def play_strategic_game():
    """
    Player 1 always start middle
    Otherwise, both players place random markers
    """
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            board = random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner    

play_strategic_game()

#Exercise 13
start_time = time.time()

games = 1000
result_strat = []

for i in range(games):
    result_strat.append(play_strategic_game()) 
                                                                           
end_time = time.time()

print(end_time - start_time)

plt.hist(result_strat)
plt.savefig('tictactoe_strat_hist.pdf')
plt.show()

#Result:
"""
Starting in the middle square is an advantage when other moves are random
Each game takes less time since victory is sooner 
Player 1 wins significantly more times than Player 2 and draws are less common.
"""