import urllib
import json

urlToParse = raw_input("Enter URL: ")
if(len(urlToParse)<1):
    urlToParse = "http://python-data.dr-chuck.net/comments_42.json"
try:
    print "Retrieving: ", urlToParse
    handle = urllib.urlopen(urlToParse)
except:
    print "Coundn't open url"
    quit()

data = handle.read()
print "Retrieved Characters: ", len(data)

jsonData = json.loads(data)
comments = jsonData["comments"]

totalSum = 0
totalCount = 0
for comment in comments:
    totalSum = totalSum + int(comment["count"])
    totalCount = totalCount + 1

print "Count: ", totalCount
print "Sum: ", totalSum
        