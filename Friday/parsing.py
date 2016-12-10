#!/usr/bin/python
# -*- coding: cp1251 -*-

from pyparsing import *
import webbrowser

optionAnswer = ['answer:', 'openPage:', 'restart', 'test', 'insert_element:']

def ParseAnswer(s, ui):
	s = s.decode('utf-8')
	s = s.split('***')
	for word in s: #тут уже нужен протокол комманд
		if word.find(optionAnswer[0]) != -1:
			ui.outputresponse(word[len(optionAnswer[0]):])
		if word.find(optionAnswer[1]) != -1:
			url = word[len(optionAnswer[1]):]
			try:
				webbrowser.open('http://' + url)
			except:
				ui.outputresponse("I'm sorry. I couldn't open your webbrowser :( ")