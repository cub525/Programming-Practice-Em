# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:53:26 2021

@author: janih
"""

import re
from typing import Dict
from dataclasses import dataclass, field
bags = {}

@dataclass(unsafe_hash=True)
class Bag(object):
    color: str
    contents: Dict[str, int] = field(default_factory=dict)

    def total_contents(self):
        total = 0
        for key in self.contents:
            # print(bags[key])
            total +=  (bags[key].total_contents()+1)*self.contents[key]
        return total

parent_comp = re.compile('(\w+\s\w+) bags contain')
child_comp = re.compile('\d (\w+\s\w+) bag')
number_comp = re.compile('(\d) \w+\s\w+ bag')

with open('input_day_7.txt', 'r') as f:
    for line in f:
        bag_color = parent_comp.match(line).group(1)
        children = child_comp.findall(line)
        inner_bags = map(Bag, children)
        contents = dict(zip(children ,map(int, number_comp.findall(line))))
        bags[bag_color] = Bag(bag_color, contents)
        

test = bags["shiny gold"].total_contents()

#%%
valid_bags = {'shiny gold'}
#%%
# for _ in range(10):
#     for key in relationships:
#         # if key in valid_bags:
#         if not relationships[key].isdisjoint(valid_bags):
#             valid_bags.add(key)
#     print(len(valid_bags))
#%%
