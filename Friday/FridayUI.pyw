

import sys
from PyQt4 import QtGui, QtCore
import FridayClient

class MainWindow(QtGui.QMainWindow):
	flag = True
	def __init__(self, httpServ, parent=None):
		super(MainWindow, self).__init__(parent)

		
		self.browser = QtGui.QListWidget()
		self.textEdit = QtGui.QLineEdit()
		self.textEdit.setMaximumSize(QtCore.QSize(400,60))
		self.connect(self.browser, QtCore.SIGNAL("returnPressed()"), self.sendrequest)

		SendButton = QtGui.QPushButton('Send')
		SendButton.setMaximumSize(QtCore.QSize(400,60))
		SendButton.clicked.connect(self.sendrequest)
		
		ExitButton = QtGui.QPushButton('Exit')
		ExitButton.setMaximumSize(QtCore.QSize(400,60))
		ExitButton.clicked.connect(httpServ.close)
		self.connect(ExitButton, QtCore.SIGNAL('clicked()'), self.close)
		
		layoutINlayout = QtGui.QHBoxLayout()
		layoutINlayout.addWidget(self.textEdit)
		layoutINlayout.addWidget(SendButton)
		layoutINlayout.addWidget(ExitButton)


		widget = QtGui.QWidget()
		self.setCentralWidget(widget)

		self.layout = QtGui.QVBoxLayout()
		self.layout.addWidget(self.browser)

		mainwindow = QtGui.QVBoxLayout()
		mainwindow.addLayout (self.layout )
		mainwindow.addLayout (layoutINlayout )

		widget.setLayout(mainwindow)
		self.setWindowFlags(QtCore.Qt.WindowTitleHint )
		
	def sendrequest(self, ):
		txt = self.textEdit.text()
		if txt != '':
			item = QtGui.QListWidgetItem(txt)
			item.setTextAlignment(2)
			self.browser.addItem(item)
			httpServ.sendrequest(txt, self)

	def outputresponse(self, txt):
		item = QtGui.QListWidgetItem(txt)
		item.setTextAlignment(1)
		self.browser.addItem(item)
	
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
widget.setWindowTitle('Qt App')
widget.show()

sys.exit(app.exec_())