import sys
from PyQt4.QtGui import * # компоненты интерфейса
from PyQt4.QtCore import *

class App(QApplication):
	def __init__(self, parent = None):
		QApplication.__init__(self, parent)
		widget = QWidget()
		widget.resize(320, 240) # изменить размеры виджета
		widget.setWindowTitle("Hello, World!") # установить заголовок
		widget.show() # отобразить окно на экране
	

	

app = App(sys.argv)
sys.exit(app.exec_()) # запуск основного цикла приложения