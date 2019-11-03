# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 19:57:07 2019

@author: Owner
"""

from zipfile import ZipFile
import re
from os import remove

with ZipFile("channel.zip",'r') as zipObj:
   zipObj.extractall()

filename = "90052.txt"
exp = re.compile(r"Next nothing is ([0-9]+)")
comment = ""
while True:
    try:
        comment += zipObj.getinfo(filename).comment.decode("utf-8")
        with open(filename) as file:            
            test = "".join(file.read().split("\n"))
       
        match = exp.findall(test)
        if len(match)>1:
            print(match)
        filename = match[-1] + ".txt"
        
    except KeyboardInterrupt:
        raise
    
print(comment)    
        

