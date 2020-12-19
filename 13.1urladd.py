"""Scraping Numbers from HTML using BeautifulSoup In this assignment you will
write a Python program similar to #http://www.py4e.com/code3/urllink2.py#.
The program will use urllib to read the HTML from the data files below, and parse
the data, extracting numbers and compute the sum of the numbers in the file."""



lst = list()

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')  #http://py4e-data.dr-chuck.net/comments_243801.html
html = urlopen(url, context=ctx).read() #open & read url
soup = BeautifulSoup(html, "html.parser") #parsing the url with BeautifulSoup

# Retrieve all of the span and than get content
tags = soup('span') # Retrieve all of the span
for num in tags:
    contents = num.contents[0] # it will retrieve numbers(currently string) from span tag
    intgr = int(contents) #converting string numbers into integers
    lst.append(intgr) #appending into list so that can be added
print(sum(lst))
