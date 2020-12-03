# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:00:30 2020

@author: janih
"""

multiple = 1

for i in [1,3,5,7]:
    location = 0
    tree_count = 0
    with open('input_day_3.txt','r') as f: 
        for line in f:
            if line[location] == '#':
                # line1 = line[:location] + 'X' + line[location+1:]
                tree_count += 1
            # else:
            #     line1 = line[:location] + '0' + line[location+1:]
            # print(line1)
            location = (location + i) % 31
    print(tree_count)
    multiple *= tree_count

#%%
    
location = 0
tree_count = 0
row = 0
with open('input_day_3.txt','r') as f: 
    for line in f:
        if row % 2 == 0:
            if line[location] == '#':
                # line1 = line[:location] + 'X' + line[location+1:]
                tree_count += 1
            # else:
            #     line1 = line[:location] + '0' + line[location+1:]
            # print(line1)
            location = (location + 1) % 31
        row +=1
            
    
print(tree_count)
multiple *= tree_count
print(multiple)