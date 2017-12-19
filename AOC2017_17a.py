#!/usr/bin/env python

stepcnt = 394

circbuf = [0]
currpos = 0

for i in range(2017):
    currpos = (currpos + stepcnt) % len(circbuf)
    circbuf.insert(currpos+1, i+1)
    currpos += 1
    if i == 2016:
        print circbuf[currpos+1]
