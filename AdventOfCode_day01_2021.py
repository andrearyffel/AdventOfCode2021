# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:03:46 2021

@author: andie

AdventOfCode Day1
"""


#%%

### Puzzle 1

inputfile = 'C:/Users/andie/Documents/PythonScripts/AdventOfCode_2021/day_01_input.txt'

depths = list()                         # Create an empty list to fill with depth numbers

with open(inputfile) as f:              # Read the input file
    lines = f.readlines()               # Read each line as a string
    for line in lines:                  # For each line:
        depths.append(int(line))        # Convert the string to an int and stor it in the list

counter = 0                             # Create a counter to store the number of increases
depth0 = depths[0]                      # Store the first depth value

for depth in depths:                    # For each list entry
    if depth > depth0:                  # If the entry is bigger than the stored value:
        counter = counter + 1           # Increase the counter by 1
    depth0 = depth                      # Store the current depth for comparison in the next round
        
print('Number of increases:', counter)

### Puzzle 2

counter2 = 0
for index, depth in enumerate(depths[0:-3]):
    if depth < depths[index+3]:
        counter2 +=1
    
print('Number of increases with moving window:', counter2)

#%%
# Andy's shiny code, adapted with enumerate:
    
with open('day1.txt', 'r') as file:
    with open('day1.txt', 'r') as file:
        depths = list(map(int, file.readlines()))

deeper1=0
deeper2=0

for i in range(len(depths)-1):

    if int(depths[i]) < int(depths[i+1]):
        deeper1 += 1

    if i < (len(depths)-3) and int(depths[i]) < int(depths[i+3]):
        deeper2 += 1

print(deeper1)
print(deeper2)


#%%

### Andrea's beginner version without enumerate but with lazy sums:

counter2 = 0                            # Counter for Puzzle 2

depthsum = sum(depths[0:3])             # Sum up the first three entries
depthlength = len(depths)
position = 0


for depth in depths[0:-2]:              # Stop the iteration after 3rd last entry
    position2 = position + 3
    depthsum2 = sum(depths[position:position2])   # Sum up this and the next two entries
    print(position, position2, depthsum2)
    if depthsum2 > depthsum:        # Compare to the stored sum, continue like in Puzzle 1
        counter2 = counter2 + 1
        print(counter2)
    depthsum = depthsum2
    position = position + 1

print('Number of increases with moving window:', counter2)



