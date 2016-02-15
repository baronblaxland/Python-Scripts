# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

from bs4 import BeautifulSoup
import urllib

url = raw_input('Enter - ')
link_poition = int(raw_input('Link Position:'))
Number_repeats = int(raw_input('Number of Repeats:'))


for x in range (0,Number_repeats):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    y=[]
# Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        y.append(tag.get('href', None))

    url = y[link_poition-1]
print y[link_poition-1]


