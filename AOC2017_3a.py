#!/usr/bin/env python

maxv = 277678
currv = 1
x = 0
y = 0
sidelen = 1

while currv < maxv:
    currv += 1
    x += 1
    sidelen += 2
    halfside = (sidelen-1)/2
    #print halfside
    #print x,y,currv
    while y < halfside:
        #print "right"
        y += 1
        currv += 1
        if currv == maxv:
            print x,y,currv
            print abs(x)+abs(y)
            break
    while x > -halfside:
        #print "top"
        x -= 1
        currv += 1
        if currv == maxv:
            print x,y,currv
            print abs(x)+abs(y)
            break
    while y > -halfside:
        #print "left"
        y -= 1
        currv += 1
        if currv == maxv:
            print x,y,currv
            print abs(x)+abs(y)
            break
    while x < halfside:
        #print "bottom"
        x += 1
        currv += 1
        if currv == maxv:
            print x,y,currv
            print abs(x)+abs(y)
            break
