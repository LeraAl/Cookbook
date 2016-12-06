

import sys
from PyQt4 import QtGui, QtCore
import FridayClient

class MainWindow(QtGui.QMainWindow):
	flag = True
	def __init__(self, httpServ, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setWindowTitle('Friday')
		self.styleData = ''
		f = open('friday.stylesheet' , 'r')
		self.styleData = f.read()
		f.close()
		self.setStyleSheet( self.styleData )
		
		self.browser = QtGui.QListWidget()
		self.browser.setWordWrap( True )
		#self.browser.setWrapping( True )
		#self.browser.setFlow( QtGui.QListView.LeftToRight )
		#self.browser.setResizeMode(QtGui.QListView.Adjust)
		#self.browser.setViewMode(QtGui.QListView.ListMode)
		self.textEdit = QtGui.QLineEdit()
		self.textEdit.setMaximumHeight(60)
		self.textEdit.setPlaceholderText('Text input...')
		self.connect(self.textEdit, QtCore.SIGNAL('editingFinished()'), self.sendrequest)
		

		SendButton = QtGui.QPushButton('Send')
		SendButton.setMaximumSize( QtCore.QSize(400,60) )
		SendButton.clicked.connect( self.sendrequest )
		
		
		layoutINlayout = QtGui.QHBoxLayout()
		layoutINlayout.addWidget( self.textEdit )  
		layoutINlayout.addWidget( SendButton )


		widget = QtGui.QWidget()
		self.setCentralWidget( widget )

		self.layout = QtGui.QVBoxLayout()
		self.layout.addWidget( self.browser )

		mainwindow = QtGui.QVBoxLayout()
		mainwindow.addLayout ( self.layout )
		mainwindow.addLayout ( layoutINlayout )

		widget.setLayout( mainwindow )
	
	#отправка ответа на сервер
	def sendrequest(self, ):
		txt = self.textEdit.text()
		if txt != '':
			requesttext = QtGui.QListWidgetItem(txt.strip())
			requesttext.setTextAlignment(2)
			requesttext.width = self.browser.gridSize().width()
			self.browser.addItem(requesttext)
			self.browser.scrollToBottom()
			self.textEdit.clear()
			httpServ.sendrequest(txt, self)

	#вывод ответа		
	def outputresponse(self, txt):
		responsetext = QtGui.QListWidgetItem(txt)
		responsetext.setBackgroundColor(QtGui.QColor(32, 32, 32, 20))
		responsetext.setTextAlignment(1)
		responsetext.width = self.browser.gridSize().width()
		self.browser.addItem(responsetext)
		self.browser.scrollToBottom()
	
	#изменение размеров сообщений в чате при изменении размеров окна
	def ResizeEvent(self, event):
		for i in range(self.browser.count):
			itemAt(i).width = self.browser.gridSize().width
	
	#перехват закрытия окна и завершение  сеанса
	def CloseEvent(self, event):
		httpServ.close()
		self.windowClose.emit()
try:
	httpServ = FridayClient.HTTPServer()
	
except:
	httpServ = 0
app = QtGui.QApplication(sys.argv)
widget = MainWindow(httpServ)
widget.resize(250, 150)
widget.show()

sys.exit(app.exec_())