import xml.etree.ElementTree as ET
import urllib

urlToParse = raw_input("Enter URL: ")
if(len(urlToParse)<1):
    urlToParse = "http://python-data.dr-chuck.net/comments_42.xml"
try:
    print "Reading: ", urlToParse
    handle = urllib.urlopen(urlToParse)
except:
    print "Coundn't open url"
    quit()

data = handle.read()

print "Retrieved Characters: ", len(data)
parsedData = ET.fromstring(data)
allCounts = parsedData.findall(".//count")

totalSum = 0
totalValues = 0

for eachCount in allCounts:
    totalSum = totalSum + int(eachCount.text)
    totalValues = totalValues +1

print "Count: ", totalValues
print "Sum: ", totalSum