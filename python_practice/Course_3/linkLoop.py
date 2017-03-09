import urllib
from bs4 import *

try:
    loopCount = int(raw_input("Enter loop count: "))
    position = int(raw_input("Enter link read position: "))
except: 
    print "Invalid integer data"
    quit()
    
siteLink = raw_input("Enter Start Url: ")

if len(siteLink)<1:
    siteLink = "http://python-data.dr-chuck.net/known_by_Maxx.html "

for i in range(loopCount):
    try:
        print "Retrieving: ", siteLink
        html = urllib.urlopen(siteLink).read()
    except:
        print "Couldn't open URL to read"
        quit()
        
    beautiful = BeautifulSoup(html,"html.parser")
    refTags = beautiful('a')
    refTagPos = refTags[position-1]
    href = refTagPos.get("href",None)
    personName = refTagPos.contents[0]
    if href is None:
        print("Cannot drill to the level mentioned")
        quit()
    siteLink = href
print personName