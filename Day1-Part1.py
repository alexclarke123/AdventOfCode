from os import read


with open("AdventOfCode/Day 1 Inputs.txt" , 'r') as f:
    lines = f.readlines()


count = 0
previousline = 0
currentline = 0

for currentline in lines:
    
  if previousline != 0: 
    if int(currentline) > int(previousline): 
        count += 1 
    previousline = currentline

print(count)
