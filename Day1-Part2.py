from os import read
from collections import deque

with open("AdventOfCode/Day 1 Inputs.txt" , 'r') as f:
    lines = f.readlines()

q1 = deque()
q2 = 0

countlines = 0
countset = 0
check = 0

for currentline in lines:
   if countset < 3: 
        q1.append(int(currentline))
        countset += 1        
   elif countset == 3:
        q2 = sum(q1)
        q1.popleft()
        q1.append(int(currentline))
        if sum(q1) > q2:
            countlines += 1 
        else: 
            check +=1

print(countlines)
print(check)

