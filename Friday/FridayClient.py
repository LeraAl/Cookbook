# -*- coding: utf-8 -*-
import http.client as httplib

def printText(txt):
    lines = txt.decode('utf-8').split('\n')
    for line in lines:
        print (line.strip())

		
server = input('Input the server:\n')	
server = server + '.ngrok.io'	
httpServ = httplib.HTTPConnection(server)
httpServ.connect()

request = input('input your request: \n')
request = 'user:' + request
print (request)
httpServ.request('POST', '/index', request.encode('utf-8'))

response = httpServ.getresponse()
if response.status == httplib.OK:
    printText (response.read())

httpServ.close()