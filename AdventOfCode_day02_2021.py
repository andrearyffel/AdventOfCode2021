# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 07:22:45 2021

@author: andie
"""

inputfile = 'C:/Users/andie/Documents/PythonScripts/AdventOfCode_2021/day_02_input.txt'

course = list()

with open(inputfile) as file:
    lines = file.readlines()
    for line in lines:
        instruction = line.lstrip(' ')
        instruction = instruction.rstrip('\n')
        print('Instruction:', instruction)
        direction = instruction.split(' ')[0]
        print('Direction:', direction)
        distance = instruction.split(' ')[1]
        print('Distance:', distance)
        course.append([direction, int(distance)])

print('Course:', course)

#%%
# Puzzle 1

forward = 0
up = 0
down = 0

for instruction in course:
    print(instruction)
    if instruction[0] == 'forward':
        forward = forward + instruction[1]
    if instruction[0] == 'up':
        up = up + instruction[1]
    if instruction[0] == 'down':
        down = down + instruction[1]                     
print('Forward:', forward, '\nUp:', up, '\nDown:', down)
result = (forward*(down-up))
print('Result:', result)

#%%
# Puzzle 2

forward = 0
up = 0
down = 0
aim = 0
depth = 0

'''
aim = aim + down
aim = aim - up
depth = depth + aim * forward
'''
for instruction in course:
    print(instruction)
    if instruction[0] == 'forward':
        forward = forward + instruction[1]
        depth = depth + (aim * instruction[1])
        print('f:', forward, 'd:', depth, 'a:', aim)
    if instruction[0] == 'up':
        #up = up + instruction[1]
        aim = aim - instruction[1]
        print(aim)
    if instruction[0] == 'down':
        #down = down + instruction[1]
        aim = aim + instruction[1]
        print(aim)

print('Forward:', forward, '\nAim:', aim, '\nDepth:', depth)
result = (forward*depth)
print('Result:', result)





         