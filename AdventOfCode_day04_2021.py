# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 08:14:44 2021

@author: andie
"""
#%%

import numpy as np
file = 'day_04_input.csv'

# Separate draws (into a list) and boards (into a numpy array)
draws=list()
with open(file, 'r') as everything:
    data = everything.readlines()
for line in data[0:1]:
    header = line.rstrip('\n')
    drawstxt = header.split(',')
    for draw in drawstxt:
        draws.append(int(draw))# 1st line of draws is stored in a list
print(draws)

boardsarray = np.genfromtxt(file, skip_header=1, dtype=int) # All boards in one array

boardcount = int(boardsarray.shape[0]/5) # The number of boards in the array

boards = boardsarray.reshape(boardcount,5,5)
print(boards)

#%%
checkboards = np.zeros((boardcount, 5,5), dtype=int) 
checkboards[:,:,:] = 1
is_looping = True
unchecked = 0

for draw in draws[0:]:
    checkboards[boards == draw] = 0
   
    for i, checkboard in enumerate(checkboards): 
        
        for row in range(checkboard.shape[0]):
            rowsum = sum(checkboard[row,:])
            
            if rowsum == 0:
                boardnr = i
                bingoboard = boards[boardnr]
                winningboard = bingoboard*checkboard
                print('boardnr:\n', boardnr)
                print('col found:\n', [checkboard[row]])
                print('draw:', draw)
                print('checkboard:\n', checkboard)
                print('bingoboard:\n', bingoboard)
                print('winningboard:\n', winningboard)
                print('sum:', np.sum(winningboard))
                result = draw * np.sum(winningboard)             
                is_looping = False
                break
            if not is_looping:
                break
            
        if not is_looping:
            break
        
    if not is_looping:
        break
            
        for col in range(checkboard.shape[1]):
            colsum = sum(checkboard[:,col])
            if colsum == 0:
                boardnr = boards[boards==checkboard]
                bingoboard = boards[boardnr]
                winningboard = bingoboard*checkboard
                print('col found:', checkboard[row])
                print('draw:', draw)
                print('checkboard:\n', checkboard)
                print('bingoboard\n:', bingoboard)
                print('winningboard\n:', winningboard)
                print('sum:', np.sum(winningboard))
                result = draw * np.sum(winningboard)             
                is_looping = False
                break
            
            if not is_looping:
                break
        
        if not is_looping:
            break
    if not is_looping:
        break
        
print(result)        
        
#%%

checkboards = np.zeros((boardcount, 5,5), dtype=int) 
checkboards[:,:,:] = 1
is_looping = True
unchecked = 0
boardsnr = len(checkboards[:,:,0])
print(boardsnr)
eliminatedboards = []

for draw in draws[0:]:
    checkboards[boards == draw] = 0
   
    for i, checkboard in enumerate(checkboards): 
        
        for row in range(checkboard.shape[0]):
            rowsum = sum(checkboard[row,:])
            colsum = sum(checkboard[:,row])
                        
            if rowsum == 0:
                boardnr = i
                print('eliminate:', i)
                if boardnr not in eliminatedboards:
                    eliminatedboards.append(boardnr)
                    boardsnr -= 1
                    print(boardsnr)
                    if boardsnr == 0:
                        print('boardnr:\n', boardnr)
                        print('col found:\n', [checkboard[row]])
                        print('draw:', draw)
                        print('checkboard:\n', checkboard)
                        print('bingoboard:\n', bingoboard)
                        print('winningboard:\n', winningboard)
                        print('sum:', np.sum(winningboard))
                        bingoboard = boards[boardnr]
                        winningboard = bingoboard*checkboard
                        result = draw * np.sum(winningboard)             
                        is_looping = False
                        break
                    
            if colsum == 0:
                boardnr = i
                if boardnr not in eliminatedboards:
                    eliminatedboards.append(boardnr)
                    boardsnr -= 1
                    if boardsnr == 0:
                        print('col found:', checkboard[row])
                        print('draw:', draw)
                        print('checkboard:\n', checkboard)
                        print('bingoboard\n:', bingoboard)
                        print('winningboard\n:', winningboard)
                        print('sum:', np.sum(winningboard))
                        
                        bingoboard = boards[boardnr]
                        winningboard = bingoboard*checkboard
                        result = draw * np.sum(winningboard)             
                        is_looping = False
                        result = draw * np.sum(winningboard)             
                        is_looping = False
                        break

                    if not is_looping:
                        break
            
                if not is_looping:
                    break
                
            if not is_looping:
                break
                
        if not is_looping:
            break
    if not is_looping:
        break
        
print(result)        
        
#%%