from pyparsing import *

optionAnswer = ['answer:', 'openPage:', 'restart', 'test', 'insert_element:']

def ParseAnswer(s, ui):
	s = s.decode('utf-8')
	s = s.split('***')
	for word in s: #тут уже нужен протокол комманд
		if word.find(optionAnswer[0]) != -1:
			ui.outputresponse(word[len(optionAnswer[0]):])
		if word.find(optionAnswer[1]) != -1:
			print('типа открылись гугл карты')