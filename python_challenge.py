# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:06:45 2019

@author: EOL
"""
from collections import Counter
import re
import urllib3

def translate_string(n,string):
    alphabet_ord = [i for i in range(97,123)]
    alphabet_str = [chr(i) for i in range(97,123)]
    #Shift list and make dictionary
    renum_ord = [alphabet_str[i+(n-26)] for i in range(len(alphabet_str))]
    dict1 = {alphabet_ord[i]:renum_ord[i] for i in range(len(alphabet_str))}
    test = str(string).translate(dict1)
    print(test)

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
    try:
        while 1:
            http = urllib3.PoolManager()
            r = http.request('GET',initial_url)
            datr = r.data.decode("utf-8")
            try:
                dat = int(''.join([i for i in datr if i.isdigit()]))
                initial_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}'.format(dat)
            except ValueError:
                print(datr)
                print(dat1)
            dat1 = dat
            
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
#    translate_string(2,'map')
    web_lookup('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022')