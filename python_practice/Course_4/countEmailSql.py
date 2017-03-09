import sqlite3
import urllib

conn = sqlite3.connect('PythonDB.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

urlLink = raw_input('Enter url: ')
if ( len(urlLink) < 1 ) : urlLink = 'http://www.pythonlearn.com/code/mbox.txt'
try:
    print "Retrieving: ", urlLink
    handle = urllib.urlopen(urlLink)
except:
    print "Coundn't open url"
    quit()

for line in handle:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        #print "Not found: ", org
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
