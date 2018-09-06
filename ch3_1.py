#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:36:45 2018

@author: coledoug
"""
# First practice problem
print('Type in an integer')

spam = input()

if spam == "1":
    print('Hello')
elif spam == "2":
    print('Howdy')
else:
    print('Greetings!')



# Another practice problem

for i in range (1,11):
    print(i)
    

# And another
x = 0
while x < 10:
    print(x + 1)
    x = x + 1