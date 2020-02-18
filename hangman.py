# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 09:35:52 2020

@author: EOL
"""
import re
import random

dictionary_name = "Collins Scrabble Words (2015).txt"

def word_list(dictionary_name):
    # Open the dictionary file and read in the words
    with open(dictionary_name,'r') as f:
        words = f.read().lower().split('\n')
        return words
    
dictionary = word_list(dictionary_name)
word = random.choice(dictionary)
x = 6
gl = []

neword = len(word)*[' _']
print(''.join(neword))
try:
    while x>0 and ''.join(neword) != word:
        g = input('Guess a letter:')
        if re.search(str(g),word) == None:
            print('That\'s not in the word')
            x = x-1
            gl.append(g)
            print(gl)
        else:
            neword[:] = [g if i == g else neword[word.index(i)] for i in word]
            print(''.join(neword))
except KeyboardInterrupt:
    pass
if x == 0:
    print('You lose')
    print(word)
else:
    print('You win')