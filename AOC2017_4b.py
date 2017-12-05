#!/usr/bin/env python

import itertools

icount = 0
rcount = 0

with open('input4b.txt') as f:
    for row in f:
        rcount += 1
        nlist = row.split()

        for a,b in itertools.combinations(nlist,2):
            #print a,b
            if len(a) == len(b):
                if a == b:
                    # print a, b
                    # print rcount, "Invalid"
                    icount += 1
                    break
                if a != b:
                    icountpre = icount
                    for c in itertools.permutations(list(a),len(a)):
                        catstr = ''.join(c)
                        if catstr == b:
                            # print a, catstr
                            # print rcount, "Invalid"
                            icount += 1
                            break
                    if icount != icountpre:
                        break

print rcount-icount
