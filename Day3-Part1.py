from os import error, read
from collections import deque
from typing import Counter

with open("AdventOfCode/Day 3 Inputs.txt" , 'r') as f:
    lines = f.readlines()

error = 0
gamma = ""  
epsilon = ""

for x in range(12):

    countOne = 0
    countZero = 0
    
    for currentline in lines:

        number = str(currentline)[x]
        if int(number) == 1:
            countOne += 1
        elif int(number) == 0:
            countZero += 1
        else: error +=1
      
    if countOne > countZero:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"    
        epsilon = epsilon + "1"    
        
consumption = int(gamma, 2) * int(epsilon, 2)
print(error)
print(consumption)


