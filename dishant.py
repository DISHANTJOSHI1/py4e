'''mport urllib
import xml.etree.ElementTree as ET

url = raw_input("Enter location: ")
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/comments_200531.xml"
print "Retrieving " + url

xml = urllib.urlopen(url).read()
print "Retrieved: " + str(len(xml)) + " characters"

tree = ET.fromstring(xml)

counts =  tree.findall('.//count')
print "Count: " + str(len(counts))

accumulator = 0

for count in counts:
    accumulator += int(count.text)

print "Sum:" + str(accumulator)'''


i=int(input("Enter a numbers to square: "))
def func(i):
    return i**2
"""
this is a strin can go multiple lines
"""
op=func(i)
print(op)



