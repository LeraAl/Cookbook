#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading

def answer(interval):
	while True:
		dataout = sock.recv(1024)
		if dataout:
			print('2: ' + dataout.decode("utf-8"))
	
def request(interval):
	while True:
		datain = input('1: ')
		if datain == 'q' or datain == 'end':
			return
		sock.send(datain.encode("utf-8"))



		
sock = socket.socket()
sock.connect(('localhost', 6668))
#data = ' '
print ('Start')

ta = threading.Thread(target=answer, args=(1,))
tr = threading.Thread(target=request, args=(1,))

ta.start()
tr.start()

sock.close()

input('Press any button...')