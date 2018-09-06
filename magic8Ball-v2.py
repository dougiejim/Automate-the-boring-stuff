#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 15:01:39 2018

@author: coledoug
"""

import random

answers = ['It is certain', 
           'It is decidedly so', 
           'Without a doubt',
           'Yes definitely', 
           'You may rely on it', 
           'As I see it, yes',
           'Most likely', 
           'Outlook good', 
           'Yes', 
           'Signs point to yes', 
           'Reply hazy, try again' 
           'Ask again later', 
           'Better not tell you now',
           'Cannot predict now', 
           'Concentrate and try again',
           'Don\'t count on it', 
           'My reply is no', 
           'My sources say no',
           'Outlook not so good', 
           'Very doubtful']

print('Ask me a question, and I\'ll tell you the future')

input()

print(answers[random.randrange(0,len(answers)-1)])