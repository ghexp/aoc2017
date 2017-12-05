#!/usr/bin/env python

import itertools

icount = 0
rcount = 0

with open('input4.txt') as f:
    for row in f:
        rcount += 1
        nlist = row.split()

        for a,b in itertools.combinations(nlist,2):
            #print a,b
            if len(a) == len(b):
                if a == b:
                    #print nlist
                    #print "Invalid"
                    icount += 1
                    break
print rcount-icount
