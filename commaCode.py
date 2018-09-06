#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Write a function that takes a list value as an argument and returns
#a string with all the items separated by a comma and a space, with 
#and inserted before the last item. For example, passing the previous 
#spam list to the function would return 'apples, bananas, tofu, and cats'. 
#But your function should be able to work with any list value passed to it.

"""
Created on Sat Jan 20 15:53:15 2018

@author: coledoug
"""

spam = ['apples', 'bananas', 'tofu', 'cats']

newString = ''

def stringReturn(list):
    newString = ''
    for i in list:
       if i != list[-1]:
           return newString + str(i +', ')
       else: 
           return newString + str(' and '+ i)
       
stringReturn(spam)

