# -*- coding: utf-8 -*-
import http.client as httplib
from parsing import *

class HTTPServer():
	httpServ = 0
	def __init__(self):
		try:
			self.httpServ = httplib.HTTPConnection('f0046207.ngrok.io')
			self.httpServ.connect()
		except:
			httpServ = 0;

	def sendrequest(self, txt, ui):
		request = "device:python_client***user:" + txt
		try:
			self.httpServ.request('POST', '/index', request.encode('utf-8'))
			self.getresponse(ui)
		except:
			ui.outputresponse("Can't connect the server")
			
	def getresponse(self, ui):	
		response = self.httpServ.getresponse()
		if response.status == httplib.OK:
			ParseAnswer(response.read(), ui)
			
	def close(self, ):
		self.httpServ.close()	