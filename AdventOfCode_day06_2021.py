# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 07:04:17 2021

@author: andie
"""

file = 'day_06_input.txt'

# Separate draws (into a list) and boards (into a numpy array)
swarm=list()
with open(file, 'r') as allfish:
    data = allfish.readlines()
for line in data:    
    fishstring = line.split(',')
    for fish in fishstring:
        swarm.append(int(fish))# 1st line of draws is stored in a list
print(swarm)

#%%
#swarm = [3,4,3,1,2]

def lanterns(n):
    for day in range(n):
        for i, fish in enumerate(swarm):
            if swarm[i] > 0:
                swarm[i] -= 1
            else:
                swarm[i] = 6
                swarm.append(9)
                      
    print(swarm)        
    print(len(swarm))
    
lanterns(80)    
#%%    
#swarm = [3,4,3,1,2]

def school(n):
    lanterns = {}
    for age in range (11):
        lanterns[age] = 0 

    for i, spawn in enumerate(swarm):
        lanterns[swarm[i]] += 1
        
    lanternfish = 0
    for day in range(n):
        lanterns[0] = lanterns[1]
        lanterns[1] = lanterns[2]
        lanterns[2] = lanterns[3]
        lanterns[3] = lanterns[4]
        lanterns[4] = lanterns[5]
        lanterns[5] = lanterns[6]
        lanterns[6] = lanterns[7] + lanterns[10]
        lanterns[7] = lanterns[8]
        lanterns[8] = lanterns[9]
        lanterns[9] = lanterns[0]
        lanterns[10] = lanterns[0]
    
    for i in range(9):
        print('i:',i)
        lanternfish += lanterns[i]
        print(lanterns)
        print(lanternfish)
        