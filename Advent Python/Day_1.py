# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:15:17 2020

@author: janih
"""

import user

with open(f'{user.path}/input.txt','r') as f:
    list_ = [int(line) for line in f]

def find_two(iterable):
    """
    Find two numbers in iterable that sum to 2020, then multiply them.
    
    Type: Function
    
    -----
    
    Parameters
    ----------
    iterable : iterable object
        
    Returns
    -------
    integer : int
        an integer equalling the multiple of the two elements

    """
    for i in iterable:
        try: 
            if iterable.index(2020 - i):
                return (2020 - i)*i
        except ValueError:
            pass
    raise ValueError('No value pair sums to 2020')

def find_three(iterable):
    for i in iterable:
        for j in iterable:
            if i != j:
                num = 2020 - i - j
                try:
                    if iterable.index(num):
                        return i*j*num
                except ValueError:
                    pass
    raise ValueError('No set of 3 Values sums to 2020')
                    
                    


if __name__ == '__main__':
    print(find_two(list_))
    print(find_three(list_))



