# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:55:40 2020

@author: janih
"""

import re
correct = 0
with open('input_day_2.txt','r') as f:
    for line in f:
        match = re.match('(\d+)-(\d+) ([a-z]):', line)
        pos1 = int(match.group(1)) + match.end()
        pos2 = int(match.group(2)) + match.end()
        letter = match.group(3)
        if  line[pos1] == letter or line[pos2] == letter and line[pos1] != line[pos2]:
            correct += 1
            print(match.group(1),pos1,line[pos1])
        