# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 07:33:01 2021

@author: andie
"""
import numpy as np

file = 'day_05_input.txt'

# Separate draws (into a list) and boards (into a numpy array)
cStart=list()
cStop=list()
with open(file, 'r') as everything:
    data = everything.readlines()
for line in data:
    wholeline = line.rstrip('\n')
    splitline = wholeline.split(' -> ')
        
    cStart.append(splitline[0].split(','))
    cStop.append(splitline[1].split(','))
 
#%% 
coordStart = np.array(cStart, dtype=int,)
coordStop = np.array(cStop, dtype=int,)
coordVec = coordStop - coordStart

print(coordStart)
print(coordStop)
print(coordVec)

#%%
#Puzzle 1:
    
flaglist = []
for x,y in coordVec[:,:]:
    if x*y == 0:
        flag = 1
    else: 
        flag = 0
    flaglist.append(flag)
    
flags = np.array(flaglist, dtype=int)   

#%%


#directions = np.stack((coordStart[flags==1], coordStop[flags==1], coordVec[flags==1]), axis = 0)
directions = np.stack((coordStart, coordStop, coordVec), axis = 0)


gridxmax = int(max(np.amax(directions[:2,:,[0]], axis=1)))+1
gridymax = int(max(np.amax(directions[:2,:,[1]], axis=1)))+1


#%%
grid = np.zeros((gridxmax, gridymax), dtype=int)
    
for i in range(directions[0,:,:].shape[0]):
#for i in range(2):
    if flaglist[i] == 1:
        x = directions[0,i,0]
        y = directions[0,i,1]
        dx = directions[1,i,0]
        dy = directions[1,i,1]
        xl = [x,dx]
        yl = [y,dy]
        xl.sort()
        yl.sort()
        xmin = xl[0]
        xmax = xl[1]+1
        ymin = yl[0]
        ymax = yl[1]+1     
        grid[xmin:xmax,ymin:ymax] +=1
    else:
        x = directions[0,i,0]
        y = directions[0,i,1]
        dx = directions[1,i,0]
        dy = directions[1,i,1]
        xl = [x,dx]
        yl = [y,dy]
        xmin = xl[0]
        xmax = xl[1]
        ymin = yl[0]
        ymax = yl[1] 

        for j in range(np.absolute(directions[2,i,0])+1):
            print(j)
            dirx = int(directions[2,i,0]/np.absolute(directions[2,i,0]))*j
            diry = int(directions[2,i,1]/np.absolute(directions[2,i,1]))*j
            pair = [x+dirx, y+diry]
                
            print(pair)
            grid[pair[0],pair[1]] += 1
          

print(grid)

show = np.where(grid>1)
shownr = len(show[0])

print(shownr)

#%%











