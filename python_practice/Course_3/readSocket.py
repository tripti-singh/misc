import socket

mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

mySocket.connect(("www.data.pr4e.org",80))
mySocket.send("GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n")

while(True):
    line = mySocket.recv(512)
    print len(line)
    if(len(line)<1):
        break
    print line
    print "PPPPPPPPRINTED"
print "here"
mySocket.close()