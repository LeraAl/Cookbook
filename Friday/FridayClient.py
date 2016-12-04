# -*- coding: utf-8 -*-
import http.client as httplib
from parsing import *

def printText(txt):
    lines = txt.decode('utf-8').split('\n')
    for line in lines:
        print (line.strip())

			
server = 'f0046207.ngrok.io'	
httpServ = httplib.HTTPConnection(server)
httpServ.connect()

request = input('input your request: \n')
request = 'user:' + request
print (request)
httpServ.request('POST', '/index', request.encode('utf-8'))

response = httpServ.getresponse()
if response.status == httplib.OK:
    ParseAnswer(response.read())

httpServ.close()