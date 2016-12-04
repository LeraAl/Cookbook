# -*- coding: utf-8 -*-
import http.client as httplib

def printText(txt):
    lines = txt.split('\n')
    for line in lines:
        print (line.strip())

		
server = input('Input the server:\n')		
httpServ = httplib.HTTPConnection(server)
httpServ.connect()

request = input('input your request: \n')
request = 'user:' + request
print (request)
httpServ.request('POST', '/index', request)

response = httpServ.getresponse()
if response.status == httplib.OK:
    printText (response.read())

httpServ.close()