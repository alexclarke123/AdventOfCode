from os import error, pipe, read
import re
from typing import final
from collections import Counter

coordslist = open('AdventOfCode/Day 5 Inputs.txt').read()
coords = [item for item in coordslist.split('\n')]

newcoords = []

for k in coords:
    j = [int(s) for s in re.findall(r'\d+', k)]

    minx = min(j[0],j[2])
    miny = min(j[1],j[3])
    maxx = max(j[0],j[2])
    maxy = max(j[1],j[3])
    
    xsign = -1 if j[2] < j[0] else 1
    ysign = -1 if j[3] < j[1] else 1
    xcount = 0 
    ycount = 0

    if minx == maxx or miny == maxy: 
            for x in range(minx, maxx + 1 ):
                for y in range(miny, maxy +1):
                    newcoords.append(str(x) + "," + str(y))   
    else:
        #if (maxx - minx) == (maxy - miny):
            for y in range(miny, maxy + 1 ):
                x = j[0] + (xcount * xsign)
                y = j[1] + (ycount * ysign)
                newcoords.append(str(x) + "," + str(y))   
                xcount += 1
                ycount += 1

coordcounter = Counter(newcoords)

mastercount = 0 

for c in coordcounter:
    if coordcounter[c] > 1:
        mastercount += 1

print(mastercount)