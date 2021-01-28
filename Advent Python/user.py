#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:52:21 2021

@author: marshallhart
"""

import os


if os.getenv("USER") == "marshallhart": 
    path = 'marshall'
else:
    path = '.'


if __name__ == '__main__':
    print(f'Input files will be read from {path}')
        
    