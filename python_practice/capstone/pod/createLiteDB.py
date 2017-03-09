import sqlite3
import re

from sqlite3 import OperationalError
from Carbon.Aliases import false

conn = sqlite3.connect("product_barcode.sqlite")
cur = conn.cursor()

cmdFile = "pod_web_2014.01.01_01.sql"

fh = open(cmdFile)
sqlCmds = fh.read()
fh.close()

sqlCommands = sqlCmds.split(';')

def sanitizeCommand(cmd):
    cmd = cmd.replace("ENGINE=InnoDB","")
    cmd = cmd.replace("DEFAULT CHARSET=utf8","")
    cmd = re.sub('AUTO_INCREMENT=[0-9]+',"",cmd) 
    cmd = cmd.replace("AUTO_INCREMENT","PRIMARY KEY AUTOINCREMENT")
    cmd = re.sub('COMMENT \'.*\'?',",",cmd)
    cmd = re.sub(',\s*KEY `[A-Z_]+` \(`[A-Z_,`]+`\)',"",cmd)
    cmd = cmd.strip()
    return cmd;

#Default i = 6
i = 6;
fullCommand=None

for command in sqlCommands[i:]:
    command = sanitizeCommand(command)
    if command == "":
        continue
    try:
        if fullCommand is None:
            fullCommand = command
        else:
            fullCommand = fullCommand + command
            print "Command incomplete, adding next line", i
        
        canExecute = False
        if fullCommand.startswith("INSERT") and (fullCommand.endswith("\')") or fullCommand.endswith("NULL)") or len(re.findall("[0-9]\)$", fullCommand))>0):
            canExecute = True
            #print "Insert Statement encountered"
        elif (not fullCommand.startswith("INSERT")) and fullCommand.endswith(")"):
            canExecute = True
            #print "NONInsert Statement encountered"
        if canExecute:
            print "Executing line: ", i
            cur.execute(fullCommand)
            conn.commit()
            fullCommand=None
        else:
            fullCommand = fullCommand+", "
        i = i + 1
    except OperationalError, msg: 
        print "Command errored: ", fullCommand, 
        print "Error: ", i, msg
        quit()
print "DONE!!!"