# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

from bs4 import BeautifulSoup

import urllib


url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

y = []

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    y.append(tag.contents[0])
    

import re

file = str(y).strip('[]')

y = re.findall('[0-9]+',file)
 
results = map(int, y)

y=sum(results)

print results

print y

