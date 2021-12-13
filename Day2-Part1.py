from os import read

with open("AdventOfCode/Day 2 Inputs.txt" , 'r') as f:
    lines = f.readlines()

count = 0
currentline = 0
horiz = 0
depth = 0
errors = 0

for currentline in lines:

  number = 0
  number = [int(i) for i in currentline.split() if i.isdigit()]
  number = sum(number)

  if currentline.find("forward") > -1: 
      horiz += number
  elif currentline.find("up") > -1:
      depth -= number
  elif currentline.find("down") > -1:
      depth += number
  else: errors += 1

distance = horiz * depth

print(distance)
print(errors)
