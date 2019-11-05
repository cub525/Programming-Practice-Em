# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:54:31 2019

@author: vaa7199
"""

import urllib3
import re

http = urllib3.PoolManager()

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
reference = ["8022"]
r = http.request("GET",url % reference[-1])
while r.status == 200:
    reference = re.findall("[0-9]+",str(r.data))
    r = http.request("GET", url % reference[-1])
    print(r.data)