import re

fname = raw_input("Enter file:")
if len(fname) < 1 : fname = "regex_sum_357928.txt"

try:
    fh = open(fname)
except:
    print "File not found"
    quit()

allNumbers = list()

for line in fh:
    trimmedLine = line.rstrip()
    numbersFound = re.findall("[0-9]+", trimmedLine)
    if len(numbersFound)==0:
        continue
    for eachNumber in numbersFound:
        allNumbers.append(int(eachNumber))
#print sum(allNumbers)
print sum( [ int(nNum) for nNum in re.findall('[0-9]+',open(fname).read()) ] )