import urllib
from bs4 import *

siteLink = raw_input("Enter Url")

if len(siteLink)<1:
    siteLink = "http://python-data.dr-chuck.net/comments_357933.html"

try:
    html = urllib.urlopen(siteLink).read()
except: 
    print "Couldn't open URL to read"
    quit()

beautiful = BeautifulSoup(html, "html.parser")

refTags = beautiful('span')

numTracker = list()

for eachTag in refTags:
    numbr = int(eachTag.contents[0])
    numTracker.append(numbr)
print sum(numTracker)