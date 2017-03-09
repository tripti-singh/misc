import xml.etree.ElementTree as ET
import sqlite3
from Carbon.Aliases import false

conn = sqlite3.connect("triptitunes.sqlite")

mycur = conn.cursor()

mycur.execute('''
CREATE TABLE IF NOT EXISTS Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
)''')
mycur.execute('''
CREATE TABLE IF NOT EXISTS Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
)''')
mycur.execute('''
CREATE TABLE IF NOT EXISTS Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
)''')
mycur.execute('''
CREATE TABLE IF NOT EXISTS Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)''')
mycur.execute('''DELETE FROM Artist;''')
mycur.execute('''DELETE FROM Genre;''')
mycur.execute('''DELETE FROM Album;''')
mycur.execute('''DELETE FROM Track;''')

#fname = raw_input("Enter XML Library file: ")
#if ( len(fname) < 1 ) : 
fname = "tracks/Library.xml"

myxml = ET.parse(fname)

def getData(haystack, needle):
    found = False
    for inTag in haystack:
        if found == True: return inTag.text 
        if inTag.tag == 'key' and inTag.text == needle:
            found=True
    return None

dictData = myxml.findall('dict/dict/dict')

for entry in dictData:
        if getData(entry, 'Track ID') is None: continue
        
        name = getData(entry, 'Name')
        artist = getData(entry, 'Artist')
        album = getData(entry, 'Album')
        genre = getData(entry, 'Genre') if getData(entry, 'Genre') is not None else ' '
        count = getData(entry, 'Play Count') if getData(entry, 'Play Count') is not None else '0'
        rating = getData(entry, 'Rating') if getData(entry, 'Rating') is not None else '-1'
        length = getData(entry, 'Total Time')
        
        if name is None or artist is None or album is None:
            continue
        
        print name, artist, album, genre, count, rating, length

        mycur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
        mycur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
        artist_id = mycur.fetchone()[0]
        
        mycur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
        mycur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
        genre_id = mycur.fetchone()[0]
        
        mycur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
        mycur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
        album_id = mycur.fetchone()[0]
        
        mycur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?,? )''', ( name, album_id, genre_id, length, rating, count ) )
        
        conn.commit()
