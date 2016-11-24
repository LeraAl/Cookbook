#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.bind(('', 6668))
sock.listen(2)
conn1, addr1 = sock.accept()
conn2, addr2 = sock.accept()

print ('1 - connected: ', addr1)
print ('2 - connected: ', addr2)

while True:
	data1 = conn1.recv(1024)
	data2 = conn2.recv(1024)
	
	if data1 == b'q':
		conn2.send('1st client is not here'.encode("utf-8"))
	if data2 == b'q':
		conn1.send('2nd client is not here'.encode("utf-8"))
	
	if (data1 == b'end') or (data2 == b'end') :
		break
	conn1.send(data2)
	conn1.send(data1)

conn.close()