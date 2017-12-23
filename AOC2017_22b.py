#!/usr/bin/env python

import numpy as np

def move(xin,yin,heading):
    x = xin
    y = yin
    if head == 0:
        y -= 1
    elif head == 1:
        x += 1
    elif head == 2:
        y += 1
    elif head == 3:
        x -= 1
    else:
        print 'error'
    return x,y

gridmax = 1000
gridoffset = 500
grid = np.zeros((gridmax,gridmax), dtype=np.int8)

with open('input22.txt') as sfile:
    for idx,fstring in enumerate(sfile):
        rowlen = len(fstring.strip())
        inflist = [n+gridoffset for n in range(rowlen) if fstring.find('#', n) == n]
        grid[idx+gridoffset, inflist] = 1

#rowlen must be odd
startx = gridoffset + (rowlen-1)/2
starty = gridoffset + (rowlen-1)/2
# print startx,starty
infcount = 0
stepcnt = 0
stepmax = 10000000

x = startx # 0-based
y = starty # 0-based
head = 0 # updir, rotate right, clockwise (+1 mod 3)

#print grid[gridoffset:gridoffset+9, gridoffset:gridoffset+9]

for step in range(stepmax):
    # print grid[gridoffset-2:gridoffset+4, gridoffset-2:gridoffset+4]
    # print x,y, head
    if grid[y,x] == 0:
        # print 'found clean, weakened'
        head -= 1
        head %= 4
        grid[y,x] = 2
    elif grid[y,x] == 2:
        # print 'found weakened, infected'
        grid[y,x] = 1
        infcount += 1
    elif grid[y,x] == 1:
        # print 'found infected, flagged'
        head += 1
        head %= 4
        grid[y,x] = 3
    elif grid[y,x] == 3:
        # print 'found flagged, cleaned'
        head += 2
        head %= 4
        grid[y,x] = 0
    else:
        print 'error'
    # print x,y, head, step, infcount

    x,y = move(x,y,head)
    if x >= gridmax or y >= gridmax or x < 0 or y < 0:
        print 'error', x, y
        break
print x,y, head, step, infcount
