# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:35:22 2021

@author: Emmett
"""

import cython

cpdef int test(unsigned int x):
    cdef int y = 0
    cdef int i
    for i in range(x):
        y += i
    return y

@cython.cfunc
def test1(x : cython.uint) -> cython.uint:
    y: cython.uint = 0
    i: cython.uint 
    for i in range(x):
        y += i
    return y

cpdef unsigned int test2(unsigned int x):
    return test1(x)
    