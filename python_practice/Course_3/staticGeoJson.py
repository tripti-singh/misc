import urllib
import json

serviceUrl = "http://python-data.dr-chuck.net/geojson?"
location = raw_input("Enter Location: ")
if(len(location)<1):
    location = "Ramapo College of New Jersey"
    
urlToParse = serviceUrl + urllib.urlencode({'sensor':'false', 'address':location})
try:
    print "Retrieving: ", urlToParse
    handle = urllib.urlopen(urlToParse)
except:
    print "Coundn't open url"
    quit()

data = handle.read()
print "Retrieved Characters: ", len(data)

try: jsonData = json.loads(data)
except: jsonData = None

if 'status' not in jsonData or jsonData['status'] != 'OK':
    print '==== Failure To Retrieve ===='
    print data

print jsonData["results"][0]["place_id"]