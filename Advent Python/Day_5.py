# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:56:52 2021

@author: janih
"""

trans = str.maketrans('FBLR','0101')
max_seat_id = 0
seats = []

def find_seat_id(seat):
    seat = seat.translate(trans)
    return int('0b' + seat,2)

with open('input_day_5.txt','r') as f:
    for line in f:
        seats.append(find_seat_id(line))
        if (sid := find_seat_id(line)) > max_seat_id:
            max_seat_id = sid

seats.sort()
for i in range(len(seats) - 1):
    if seats[i] + 1 != seats[i+1]:
        print(seats[i],seats[i+1])
