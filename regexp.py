# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
 
hand = open('regex_sum_199051.txt')
 
file = hand.read()

y = re.findall('[0-9]+',file)
 
results = map(int, y)

y=sum(results)

print results

print y