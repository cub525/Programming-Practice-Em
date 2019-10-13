# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:54:10 2019

@author: EOL
"""
from fractions import Fraction
def Even_Odd(n):
    #Add input clause here
    if n % 2 == 0:
        print('Your Number is Even')
    else:
        print('your number is odd')
    for i in range(10):
        print(n+2*i)
        
def mult_table(n,times):
    #add input clause here
    for i in range(1,times+1):
        print('{0} x {1} = {2}'.format(n, i, n*i))
        
'''
Here begins definitions for fraction calculator
'''
def add(a,b):
    print('result of addition: {0}'.format(a+b))
    
def subt(a,b):
    print('result of subtraction: {0}'.format(a-b))
    
def mult(a,b):
    print('result of multiplication: {0}'.format(a*b))
    
def div(a,b):
    print('result of division: {0}'.format(a/b))
    
def frac_calc():
    a = Fraction(input('Input First Fraction:'))
    b = Fraction(input('Input Second Fraction:'))
    op = input('What operation to complete: Addition (a), Subtraction (s), Multiplication (m), division(d):')
    if op == 'a':
        add(a,b)
    elif op == 's':
        subt(a,b)
    elif op == 'm':
        mult(a,b)
    elif op == 'd':
        div(a,b)
    else:
        print('invalid choice')
        

if __name__ == '__main__':
    try:
        while True:
            mult_table(5,9)
            q = input('Do you want to quit?(y,n):')
            if q == 'y':
                print('finished')
                break
    except KeyboardInterrupt:
        print('finished')
        pass