# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:57:07 2021

@author: andie
"""

pos = [16,1,2,0,4,2,7,1,2,14]

disttot = 0
#crabcount = len(pos)
distmax = max(pos)
posopt = distmax

for i in range(distmax + 1):
    for j, point in enumerate(pos):
        disttot = 0
        disttoI = abs(i - pos[j])
        print(disttoI)
        disttot += disttoI
        if disttot < posopt:
            posopt = disttot
            
    print(i, disttot)
print('Optimal position:', posopt)    


for i, point in enumerate(pos):
    print(i)
    #disttopos = 16-16 + 16-1 + 16-2 + 16-0 = 0 + 15 + 14 + 16
    disttopos = pos[i]*(len(pos)-(pos[i]-disttot))
    print(pos[i])
    print(disttopos)



for i, point in enumerate(pos):
    print(i)
    print(point)
    print(disttot-i)
    dist = disttot - 2*pos[i]
    print(dist)
    if dist < posmarker:
        posmarker = dist
print(posmarker)
    