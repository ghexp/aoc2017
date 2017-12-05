#!/usr/bin/env python

import pandas as pd
import numpy as np
import itertools

sraw = pd.read_clipboard(header=None)
narray = sraw.as_matrix()
#print narray

total = 0
nrows = narray.shape[0]
for row in range(nrows):
    comboiter = itertools.combinations(narray[row,:],2)
    for a, b in comboiter:
        if ( max(a,b) % min(a,b) ) == 0:
            total = total + ( max(a,b) / min(a,b) )

print total

total = 0
for row in range(narray.shape[0]):
    total = total + ( max(narray[row,:]) - min(narray[row,:]) )
print total
