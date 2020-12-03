# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:15:17 2020

@author: janih
"""

with open('input.txt','r') as f:
    list_ = [int(line) for line in f]

for i in list_:
    for j in list_:
        if i != j:
            try:
                num = 2020 - i - j
                if list_.index(num):
                    print(i*j*num)
                    break
                break    
            except ValueError:
                pass
        