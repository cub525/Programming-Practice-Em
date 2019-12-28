# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 16:09:46 2019

@author: vaa7199
"""

a = ['1', '11', '21', '1211', '111221']

for n in range(5,31,1):
    a.append(a[n-1]+a[n-2])