# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:46:31 2021

@author: andie
"""

#%%

import numpy as np

inputfile = 'day_03_input.csv'

diagnostics = []
colsum = 0
colsums = []

with open(inputfile) as file:
    data = file.readlines()

for line in data:
    diagnostics.append(line.rstrip('\n'))

for i,binary in enumerate(diagnostics[0:2]):
    print(binary)
    
for j,cipher in enumerate(diagnostics[0:1]):
    print(cipher)
    colsum += int(cipher)
    print(colsum)
    colsums.append(colsum)
    colsum = 0
print(colsums)

#%%
diagStr = np.loadtxt(inputfile, dtype=str)  #loads a csv with strings using tabs as delimiter

rows = len(diagStr) #nr of rows
columns = len(diagStr[1]) # nr of letters in first row = nr of cols
commons = rows/2  # to find out which is the most common number

gamma = str()
epsilon = str()

# this creates an empty array with a col for each letter
diagarray = np.zeros((rows, columns), dtype=int) 

 
for i,binary in enumerate(diagStr):     # i = for each row
    for j,letter in enumerate(binary):   # j = for each letter in a given row
        number = int(letter)    # make every letter a number
        diagarray[i,j] = number # my empty array is being filled up with numbers in the proper position

# Now I loop through my array filled with integers:
for col in range(diagarray.shape[1]): # the .shape addresses rows [0] or numbers[1]
    total = sum(diagarray[:,col])   # summing up all 1s in a row
    if total > commons: # next lines are converting numbers back to string for binary string
        gammaNr = str(1)
        epsilonNr = str(0)
    elif total < commons:
        gammaNr = str(0)
        epsilonNr = str(1)
    gamma += gammaNr 
    epsilon += epsilonNr

power = int(gamma,2)*int(epsilon,2) # returning binary to int and multiplying
print(power)

#%%

# in part 2 I loop to the array by column and remove unwanted rows, then loop through the next column

# Oxygen generator rating:
    
oxygr = np.copy(diagarray)  #create a copyof my array for safety
gammabin = str()

    
for col in range(oxygr.shape[1]):   # .shape[1] addresses all columns .shape[0] addresses rows
    total = sum(oxygr[:,col])   # sum(: = all rows, col = current column)
    if total >= commons:
        gammaNr = 1
    else: gammaNr = 0
# the next instruction loops through all rows and keeps the ones where the current columnvalue == gammaNr    
    oxygr = oxygr[oxygr[:,col] == gammaNr,:]
# now that all unwanted rows have been removed I again calculate the most common value   
    commons = oxygr.shape[0]/2
    if oxygr.shape[0] ==1: # I stop as soon as I have only one row left
        break

for col in range(oxygr.shape[1]):   #loop through each column of my one row that is left
    print(str(oxygr[0,col]))    
    gammabin +=(str(oxygr[0,col]))  #create my binary string by adding each number as letter

gamma = int(gammabin,2)
print(gammabin)
print(gamma)

# CO2 scrubber rating:    

co2sr = np.copy(diagarray)
epsilonbin = str()
    
for col in range(co2sr.shape[1]):
    total = sum(co2sr[:,col])
    if total >= commons:
        epsilonNr = 0
    else: epsilonNr = 1
    co2sr = co2sr[co2sr[:,col] == epsilonNr,:]
    commons = co2sr.shape[0]/2    
    print(commons)
    if co2sr.shape[0] ==1:
        break

for col in range(co2sr.shape[1]):
    print(str(co2sr[0,col]))    
    epsilonbin +=(str(co2sr[0,col]))

epsilon = int(epsilonbin,2)
print(epsilonbin)
print(epsilon)

print(gamma*epsilon)
