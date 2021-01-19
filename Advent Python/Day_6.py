# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:25:58 2021

@author: janih
"""
total_yes = 0
group_yes = set()
with open('input_day_6.txt','r') as f:
    for line in f:
        if line != '\n':
            person_yes = set([*line])
            if not len(group_yes):
                group_yes = person_yes
            else:
                group_yes.intersection_update(person_yes)
        else:
            group_yes.remove('\n')
            total_yes += len(group_yes)
            group_yes.clear()


print(total_yes)