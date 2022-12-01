# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:19:37 2021

@author: andie
"""
import numpy as np
file = 'day_09_test.csv'

# Separate draws (into a list) and boards (into a numpy array)

locallow = 0
heights = []

floor = np.genfromtxt(file, dtype=str, delimiter='\n') # All boards in one array

for x,y in floor[:,:]:
    heights.append(floor[x-1,y])
    heights.append(floor[x+1,y])
    heights.append(floor[x,y-1])
    heights.append(floor[x,y+1])
    if floor[x,y] < min(heights):
        locallow +=1
    
print(locallow)
    