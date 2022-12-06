from os import error, read
from collections import deque
from typing import Counter

with open("AdventOfCode/Day 3 Inputs.txt" , 'r') as f:
    lines = f.readlines()

fullset = lines[:]
error = 0

newlist = []

for run in range(2):
        
    for x in range(12):

        countOne = 0
        countZero = 0
        
        for currentline in fullset:
                number = str(currentline)[x]
                if int(number) == 1:
                    countOne += 1
                elif int(number) == 0:
                    countZero += 1
                else: error +=1
            
        if countOne < countZero:
            Common = run - 0
        elif countOne == countZero: Common = 1 - run 
        else: Common = 1 - run

        for currentline in fullset:
                number = str(currentline)[x]
                if int(number) != Common:
                    newlist.append(currentline)

        for y in newlist:
            if y in fullset:
                fullset.remove(y)
        
        newlist.clear()

        if len(fullset) == 1:
            output = int(fullset[0], 2) 
            break

    print(output)
    fullset = lines