#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 6666))
data = ' '
while True:
	data = input()
	if data == 'end':
		break
	sock.send(data.encode("utf-8"))	
	data = sock.recv(1024)
	print(data.decode("utf-8"))
sock.close()

input('Press any button...')