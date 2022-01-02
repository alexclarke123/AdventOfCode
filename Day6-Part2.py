from os import error, pipe, read
import re
from typing import final
from collections import Counter

fishlist = open('AdventOfCode/Day 6 Inputs.txt', encoding= "utf-16").read()
fishies = [int(item) for item in fishlist.split(',')]

fishcounter = Counter({0:0, 1:0, 2:0, 3:0 , 4:0, 5:0 ,6:0 , 7:0, 8:0})

fishcounter.update(fishies)
Days = 256
newfish = 0

for t in range(0, Days):

        newfish = fishcounter[0]

        for fish in (list(fishcounter)):
    
            fishcounter[fish] = fishcounter[fish + 1]
                 
        fishcounter[6] += newfish
        fishcounter[8] += newfish
 

## count the number of integers in the list
answer = sum(fishcounter.values())
print(answer)