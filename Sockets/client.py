#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading

def answer(sock):
	while True:
		dataout = sock.recv(1024)
		if dataout:
			print('\n2: ' + dataout.decode("utf-8"))
		if dataout == 'q' or dataout == 'end':
			sock.close()
			thread_answer.end()
			thread_request.end()
			input('Press any button...')
			return
	
def request(sock):
	while True:
		datain = input('1: ')
		sock.send(datain.encode("utf-8"))
		if datain == 'q' or datain == 'end':
			sock.close()
			thread_answer.end()
			thread_request.end()
			input('Press any button...')
			return



def main():		
	sock = socket.socket()
	sock.connect(('localhost', 6668))
	print ('Start')

	thread_answer = threading.Thread(target=answer, args=(sock,))
	thread_request = threading.Thread(target=request, args=(sock,))

	thread_answer.start()
	thread_request.start()

main()