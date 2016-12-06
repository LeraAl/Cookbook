

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
		self.textEdit = QtGui.QLineEdit()
		self.textEdit.setMaximumHeight(60)
		self.connect( self.browser, QtCore.SIGNAL("returnPressed()"), self.sendrequest )

		SendButton = QtGui.QPushButton('Send')
		SendButton.setMaximumSize( QtCore.QSize(400,60) )
		SendButton.clicked.connect( self.sendrequest )
		
		ExitButton = QtGui.QPushButton('Exit')
		ExitButton.setMaximumSize( QtCore.QSize(400,60) )
		ExitButton.clicked.connect( httpServ.close )
		self.connect( ExitButton, QtCore.SIGNAL('clicked()'), self.close )
		
		layoutINlayout = QtGui.QHBoxLayout()
		layoutINlayout.addWidget( self.textEdit )  
		layoutINlayout.addWidget( SendButton )
		layoutINlayout.addWidget( ExitButton )


		widget = QtGui.QWidget()
		self.setCentralWidget( widget )

		self.layout = QtGui.QVBoxLayout()
		self.layout.addWidget( self.browser )

		mainwindow = QtGui.QVBoxLayout()
		mainwindow.addLayout ( self.layout )
		mainwindow.addLayout ( layoutINlayout )

		widget.setLayout( mainwindow )
		#self.setWindowFlags( QtCore.Qt.WindowTitleHint )
		
	def sendrequest(self, ):
		txt = self.textEdit.text()
		if txt != '':
			requesttext = QtGui.QListWidgetItem(txt)
			#requesttext.setBackgroundColor(QtGui.QColor(200, 3, 32, 20))
			requesttext.setTextAlignment(2)
			self.browser.addItem(requesttext)
			httpServ.sendrequest(txt, self)

	def outputresponse(self, txt):
		responsetext = QtGui.QListWidgetItem(txt)
		responsetext.setBackgroundColor(QtGui.QColor(32, 32, 32, 20))
		responsetext.setTextAlignment(1)
		self.browser.addItem(responsetext)
	
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