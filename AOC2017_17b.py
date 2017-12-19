#!/usr/bin/env python
from numba import jit

stepcnt = 394
itermax = 50000000

# (a + b) mod n = [(a mod n) + (b mod n)] mod n.

# a mod n = a - (n * int(a/n))
@jit
def calcmax(itermax, stepcnt):
    retlist = []

    # circbuf = [0]
    currpos = 0

    for i in range(itermax):
        currpos = (currpos + stepcnt) % (i+1)
        # circbuf.insert(currpos+1, i+1)
        currpos += 1
        if currpos == 1 and i > 10000000:
            retlist.append(i+1)
    return retlist

retlist = calcmax(itermax, stepcnt)
print retlist
