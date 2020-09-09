# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:12:42 2019

@author: vaa7199
"""

import re

with open("equality.html") as file:
    html = file.read() 
    
exp = re.compile("[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]")
test = exp.findall(html)
answer = "".join([string[4] for string in test])
print(answer)