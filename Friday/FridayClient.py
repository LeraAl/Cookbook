# -*- coding: utf-8 -*-
import http.client as httplib
from parsing import *

class HTTPServer():
	httpServ = 0
	def __init__(self):
		
		self.httpServ = httplib.HTTPConnection('f0046207.ngrok.io')
		self.httpServ.connect()
	

# request = input('input your request: \n')
# request = 'user:' + request
# print (request)

	def sendrequest(self, ):
		request = "user:blablabla"
		self.httpServ.request('POST', '/index', (request).encode('utf-8'))
		self.getresponse()

	def getresponse(self, ):	
		response = self.httpServ.getresponse()
		if response.status == httplib.OK:
			ParseAnswer(response.read())
	def close(self, ):
		self.httpServ.close()	