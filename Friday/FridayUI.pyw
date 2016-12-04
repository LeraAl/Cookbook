import sys
from PyQt4 import QtGui, QtCore
import FridayClient

class MainWindow(QtGui.QMainWindow):
    def __init__(self, httpServ, parent=None):
        super(MainWindow, self).__init__(parent)

        roomLabel = QtGui.QLabel('room')

        self.browser = QtGui.QTextBrowser()
        self.browser.backwardAvailable

        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setMaximumSize(QtCore.QSize(400,60))
        #4 edit line
        self.connect(self.browser, QtCore.SIGNAL("returnPressed()"), httpServ.sendrequest)

        SendButton = QtGui.QPushButton('Send')
        SendButton.setMaximumSize(QtCore.QSize(400,60))
        SendButton.clicked.connect(httpServ.sendrequest)
		
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

httpServ = FridayClient.HTTPServer()
app = QtGui.QApplication(sys.argv)
widget = MainWindow(httpServ)
widget.resize(250, 150)
widget.setWindowTitle('Qt App')
widget.show()

sys.exit(app.exec_())