#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading

def listen(sock, conn_to_listen, conn_to_send, thread_1, thread_2):
	while True:
		data = conn_to_listen.recv(1024)
		
		if data == b'q':
			conn_to_send.send('Your friend client is not here'.encode("utf-8"))
		if data == b'end':
			conn_to_send.send(data)
			conn_to_listen.close()
			conn_to_send.close()
			thread_1.end()
			thread_2.end()
			return
			
		conn_to_send.send(data)



def main():
	sock = socket.socket()
	sock.bind(('', 6668))
	sock.listen(2)
	
	conn1, addr1 = sock.accept()
	print ('1 - connected: ', addr1)
	conn2, addr2 = sock.accept()
	print ('2 - connected: ', addr2)

	global thread_1
	global thread_2
	
	thread_1 = threading.Thread(target=listen, args=(sock, conn1, conn2, thread_1, thread_2,))
	thread_2 = threading.Thread(target=listen, args=(sock, conn2, conn1, thread_1, thread_2,))

	thread_1.start()
	thread_2.start()
	
thread_1 = threading.Thread()
thread_2 = threading.Thread()
main()