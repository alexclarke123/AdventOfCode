from os import error, pipe, read
import re
from typing import final
from collections import Counter
import statistics

crablist = open('AdventOfCode/Day 7 Inputs.txt').read()
crabpositions = [int(item) for item in crablist.split(',')]

position = statistics.median(crabpositions)
print(position)
total = 0

for k in crabpositions:

    total += abs(k - position)

print(total)