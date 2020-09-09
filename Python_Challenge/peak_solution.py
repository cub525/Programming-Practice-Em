# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 20:59:09 2019

@author: vaa7199
"""

import pickle 

#banner.p previously saved off from peak.html    
banner = pickle.load(open('banner.p','rb'))
s = "\n".join(
        [ "".join([elem[0]*elem[1] for elem in row]) for row in banner])
print(s)
