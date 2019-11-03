# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:06:45 2019

@author: EOL
"""
from collections import Counter
import re
import urllib3
from zipfile import ZipFile

def channel_solution():
    url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
    http = urllib3.PoolManager()
    r = http.request('GET',url)
    with open('channel.zip','wb') as out:
         
    print(z)
    
    
     
def translate_string(n,string):
    alphabet_ord = [i for i in range(97,123)]
    alphabet_str = [chr(i) for i in range(97,123)]
    #Shift list and make dictionary
    renum_ord = [alphabet_str[i+(n-26)] for i in range(len(alphabet_str))]
    dict1 = {alphabet_ord[i]:renum_ord[i] for i in range(len(alphabet_str))}
    # A totally equivalent line to the above (a little more pythonic, I think)
    dict2 = {number:letter for (number,letter) in zip(alphabet_ord,renum_ord)}
    test = str(string).translate(dict1)
    print(test)

def translate_string_dad(n,string):
    """
    Dad's version of Emmett's translate_string, no idea if it is actually better
    or cleaner.. just I had to work through it.
    -- Only works for lowercase... uppercase will remain unchanged
    """
    alphabet_str = [chr(i) for i in range(ord('a'),ord('z')+1)]
    alphabet_str2 = alphabet_str[:]
    #Shift list and maketrans
    for i in range(n): alphabet_str2.append(alphabet_str2.pop(0)) 
    transrule = str.maketrans(''.join(alphabet_str),''.join(alphabet_str2))
    print(string.translate(transrule))
    
def freq_in_str(string):
    chars = Counter([i for i in string])
    fq_chars = chars.most_common()
    print(fq_chars)

def type_in_string(string):
    string1 = string.replace('\n','')
    caps = ''.join([str(int(letter.isupper())) for letter in string1])
    var1 = [m.start() for m in re.finditer('011101110',caps)]
    ans = ''.join([string1[i+4] for i in var1])
    print(ans)

def web_lookup(initial_url):
    dat1 = 0
    http = urllib3.PoolManager()
    try:
        while 1:          
            r = http.request('GET',initial_url)
            datr = r.data.decode("utf-8")
            try:
                print(datr)
                dat = int(''.join([i for i in datr if i.isdigit()]))
                print(dat)
                initial_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}'.format(dat)
                print(initial_url)
            
            except ValueError:
                print(datr)
                print(dat1)
                break
            dat1 = dat
            
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
#    translate_string_dad(2,'AaBbcdefghijklmnopqrstuvwxyz')
#    translate_string(2,'AaBbcdefghijklmnopqrstuvwxyz')
#    web_lookup('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=826836357923542345463246345623452345')
    channel_solution()