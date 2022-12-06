from os import error, pipe, read
import re
from typing import final
from collections import Counter

fishlist = open('AdventOfCode/Day 6 Inputs.txt', encoding= "utf-16").read()
fishies = [int(item) for item in fishlist.split(',')]

fishcounter = Counter(fishies)

dayendfishies = []

Days = 256
newfish = 8
#countdays = 0

for t in range(0, Days):

    for index, fish in enumerate(fishies):
        
        if fish == 0:
            fishies[index] += 6
            fishies.append(newfish + 1)
        else: 
             fishies[index] -= 1

    #countdays += 1   
    print(t)
    print(len(fishies)) 
     

print(len(fishies))

## count the number of integers in the list