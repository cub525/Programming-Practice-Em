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
        # print('Age is invalid '+ field_dict_['byr'])
        # No passports have invalid ages
        return False
    elif  not 2010 <= int(field_dict_['iyr']) <= 2020:
        print('Invalid iyr ' + field_dict_['iyr'])
        return False
    elif not 2020 <= int(field_dict_['eyr']) <= 2030:
        print('Invalid eyr ' + field_dict_['eyr'])
        return False
    elif field_dict_['ecl'] not in {'amb','blu','brn','gry','grn','hzl','oth'}:
        print('Invalid ecl ' + field_dict_['ecl'])
        return False
    elif not re.match('#[a-f\d]{6}', field_dict_['hcl']):
        print('Invalid hcl ' + field_dict_['hcl'])
        return False
    elif not re.match('\d{9}', field_dict_['pid']):
        print('Invalid pid ' + field_dict_['pid'])
        
        return False
    elif 'cm' in field_dict_['hgt'] and not (150 <= int(re.match('\d+', field_dict_['hgt']).group()) <= 193):
        print('Invalid hgt '+ field_dict_['hgt'])
        return False
    elif 'in' in field_dict_['hgt'] and not (59 <= int(re.match('\d+', field_dict_['hgt']).group()) <= 76):
        print('Invalid hgt '+ field_dict_['hgt'])
        return False
    else:
        return True

def validate_passport(passport):
    valid = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
    field_dict = {i:j for i,j in re.findall('([a-z]{3}):(\S*)',passport)}
    fields = set(field_dict.keys())
    if fields.issuperset(valid):
        if validate_field(field_dict) == True:
            return True
    else:
        return False
    
    
    
with open('input_day_4.txt','r') as f:
    for line in f:
        if line != '\n':
            passport += ' ' + line[:-1]
        else:
            if validate_passport(passport) == True:
                count += 1
            passport = ''

