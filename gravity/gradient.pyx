# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:07:22 2021

@author: Emmett
"""

import cython

@cython.ccall
def test1(x : cython.uint) -> cython.uint:
    y: cython.uint = 0
    i: cython.uint 
    for i in range(x):
        y += i
    return y