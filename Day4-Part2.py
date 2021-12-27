import re
from os import error, read
from typing import Counter, final

# with open("AdventOfCode/Day 4 Inputs.txt" , 'r') as f:
#     lines = f.readlines()

boards = open('AdventOfCode/Day 4 Inputs.txt').read()
boards = [item.split() for item in boards.split('\n\n')]

set1 = boards[0]
set1 = ','.join(set1)
set1 = [int(item)  for item in set1.split(',')]

#remove the bingo numbers list to leave only the complete set of Boards
boards.pop(0) 

#set up a list to contain the details on the currently 'winning' board
currentwinningboard = ['blank'] * 3
currentwinningboard[0] = 0 

#iterate through each board
for selectedboard in boards:

    # check for bingo by rows
    bingocalleachrow = 0
    bingocallallrows = 100

    for i in range(0,5): 
        for j in range(0, 5):
            k = int(selectedboard[j+(i*5)])
            match = set1.index(k)
            bingocalleachrow = max(match, bingocalleachrow)

        bingocallallrows = min(bingocalleachrow , bingocallallrows)
        bingocalleachrow = 0

    # check for bingo by columns
    bingocalleachcol = 0
    bingocallallcols = 100

    for i in range(0,5): 
        for j in range(0, 5):
            k = int(selectedboard[i+(j*5)])
            match = set1.index(k)
            bingocalleachcol = max(match, bingocalleachcol)
        bingocallallcols = min(bingocalleachcol , bingocallallcols)
        bingocalleachcol = 0

    #save details of currently winning board
    if currentwinningboard[0] < min(bingocallallcols, bingocallallrows):
        currentwinningboard[0] = min(bingocallallcols, bingocallallrows) #position of winning number in full bingo list
        #currentwinningboard[1] = RowOrCol #was the winning line a row or column?
        currentwinningboard[2] = boards.index(selectedboard) #which number board is the current winner?


# create a list of integers for the Winning Board
winningboard = boards[currentwinningboard[2]]
winningboard = ','.join(winningboard)
winningboard = [int(item)  for item in winningboard.split(',')]

#create a list of all the bingo numbers prior to the winning numbers
del set1[currentwinningboard[0]+1:100]

winningboardremaining = [ele for ele in winningboard if ele not in set1]

finalnumber = sum(winningboardremaining) * set1[currentwinningboard[0]]
print(finalnumber)


#REDUNDANT CODE
#   # record whether columns or rows were better
#     RowOrCol = ""
#     if bingocallallcols < bingocallallrows:
#         RowOrCol = "column"
#     elif bingocallallcols > bingocallallrows:
#         RowOrCol = "row"
#     else: RowOrCol = "both"