import urllib.request as ur
import json

# json_url = 'http://python-data.dr-chuck.net/comments_42.json'

json_url = input("Enter location: ")
print("Retrieving ", json_url)
data = ur.urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

total = 0
Countt = 0

for comment in json_obj["comments"]:
    total = total + int(comment["count"])
    Countt = Countt + 1

print('Count:', Countt)
print('Sum:', total)
