# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:42:14 2020

@author: Owner
"""
def texttobi(text):
    bianary = ''.join([bin(ord(i)) for i in text])
    return bianary

def bitotext(bianary):
    text = []
    blist = []
    for i in range(len(bianary)):
        if bianary[i] == 'b':
            blist.append(i)
    blist.append(len(bianary)+1)
            
    for b in range(len(blist)-2):
        text.append(chr(int(bianary[blist[b]-1:blist[b+1]-1],2)))
    letters = ''.join(text)
    return letters

if __name__ == '__main__':
    bitotext()