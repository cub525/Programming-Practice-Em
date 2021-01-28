# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:41:06 2021

@author: janih
"""
# 11586 is too low
with open("input_day_9.txt","r") as f:
    stream = [int(line.rstrip()) for line in f]


def find_two(iterable, number):
    for i in iterable:
        try: 
            if iterable.index(number - i) and number != i:
                return (number - i),i
        except ValueError:
            pass
    raise ValueError(f'No value pair sums to {number}')

for i in range(26, len(stream)):
    find_two(stream[i-26:i-1], stream[i])