# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:42:26 2020

@author: Marshall

Experimenting with Van Eck's Sequence, A181391
"""


seq = [0]
last=dict()

N = 10**6 #Size of the sequencd to return

try:
    for n in range(1,N):
        if seq[n-1] not in last: # if we have seen this number before
            i = 0 # seq[n-1] is new number, place a zero
        else:
            i = n-last[seq[n-1]]-1
        last[seq[n-1]]=n-1 # update the record of when numbers were seen last
        seq.append(i) # stuff the new number in the sequence


except KeyboardInterrupt:
    print('interrupted!')
    
# What did I learn from this that I didn't know already...
# dictionaries with integer keys are really cool.. they index like lists without 
# a requirement of having continuous entries... kind of like a sparse matrix.