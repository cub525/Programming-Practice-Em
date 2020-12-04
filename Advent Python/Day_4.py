# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:35:37 2020

@author: janih
"""

# 204 is too low
import re
count = 0
fields = set()
passport = ''
valid = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}


def validate_field(field_dict_):
    if 1920 >= int(field_dict_['byr']) >= 2002:
        return False
    elif  not 2010 <= int(field_dict_['iyr']) <= 2020:
        return False
    elif not 2020 <= int(field_dict_['eyr']) <= 2030:
        return False
    elif field_dict_['ecl'] not in {'amb','blu','brn','gry','grn','hzl','oth'}:
        return False
    elif not re.match('#[a-f0-9]{6}', field_dict_['hcl']):
        return False
    elif not re.match('\d{9}', field_dict_['pid']):
        return False
    elif 'cm' in field_dict_['hgt']:
        if not 150 <= int(re.match('\d+', field_dict_['hgt']).group()) <= 193:
            return False
    if 'in' in field_dict_['hgt']:
        if not 59 <= int(re.match('\d+', field_dict_['hgt']).group()) <= 76:
            return False
    else:
        return True


with open('input_day_4.txt','r') as f:
    for line in f:
        if line != '\n':
            passport += ' ' + line[:-1]
        else:
            field_dict = {i:j for i,j in re.findall('([a-z]{3}):(\S*)',passport)}
            fields = set(field_dict.keys())
            if fields.issuperset(valid):
                # print(fields)
                if validate_field(field_dict):
                    count += 1
            field_dict.clear()
            fields.clear()
            passport = ''

