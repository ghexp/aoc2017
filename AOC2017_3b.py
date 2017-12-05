#!/usr/bin/env python

import pandas as pd
maxv = 277678
currv = 1
x = 0
y = 0
sidelen = 1
rowidx = range(-300,300)
colidx = range(-300,300)
grid = pd.DataFrame(np.zeros((600,600),dtype=np.int), index=rowidx, columns=colidx)
grid.loc[x,y] = currv

while sumn < maxv:
    x += 1
    sidelen += 2
    halfside = (sidelen-1)/2
    #print halfside
    adj = grid.loc[x-1:x+1,y-1:y+1]
    sumn = adj.values.sum()
    print x,y, sumn
    grid.loc[x,y] = sumn
    while y < halfside:
        #print "right"
        y += 1
        adj = grid.loc[x-1:x+1,y-1:y+1]
        sumn = adj.values.sum()
        #print x,y, sumn
        grid.loc[x,y] = sumn
        if sumn > maxv:
            print x,y, sumn
            break
    while x > -halfside:
        #print "top"
        x -= 1
        adj = grid.loc[x-1:x+1,y-1:y+1]
        sumn = adj.values.sum()
        #print x,y, sumn
        grid.loc[x,y] = sumn
        if sumn > maxv:
            print x,y, sumn
            break
    while y > -halfside:
        #print "left"
        y -= 1
        adj = grid.loc[x-1:x+1,y-1:y+1]
        sumn = adj.values.sum()
        #print x,y, sumn
        grid.loc[x,y] = sumn
        if sumn > maxv:
            print x,y, sumn
            break
    while x < halfside:
        #print "bottom"
        x += 1
        adj = grid.loc[x-1:x+1,y-1:y+1]
        sumn = adj.values.sum()
        #print x,y, sumn
        grid.loc[x,y] = sumn
        if sumn > maxv:
            print x,y, sumn
            break
    print x,y, sumn
