# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:35:22 2021

@author: Emmett
"""

cpdef int test(int x):
    cdef int y = 0
    cdef int i
    for i in range(x):
        y += i
    return y