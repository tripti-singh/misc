fruit = "banana"
print fruit[:3]

def countLetter(haystack, needle):
    count = 0
    for letter in haystack:
        if letter == needle: 
            count = count + 1
    return count

print countLetter(fruit, "n")

world = "hello. world"
print world.capitalize()

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print "Can't read file ", fname
    quit()
total = 0;
count = 0;
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    x = float(line.split(':')[1].strip())
    total = total + x 
    count = count + 1
average = total/count
print "Average spam confidence: ", average


fname = raw_input("Enter file name: ")
if len(fname)==0:
    fname = "mbox-short.txt"
#try:
fh = open(fname)
#except:
#    print "Could not open file ", fname
#    quit()
    
count = 0
for line in fh:
    if not line.startswith("From"):
        continue
    email = line.split()[1]
    print email
    count = count+1
print "There were", count, "lines in the file with From as the first word"

fname = raw_input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print "Could not open file ", fname
    quit()
    
counts = dict()
maxKey = None
maxValue = -1
for line in fh:
    if not line.startswith("From "):
        continue
    email = line.split()[1]
    counts[email] = counts.get(email,0)+1
for email in counts.keys():
    if maxValue < counts[email]:
        maxValue = counts[email]
        maxKey = email
if maxKey is not None:
    print maxKey, maxValue
