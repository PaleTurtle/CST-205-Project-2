
import sys
from PyQt5.QtWidgets import (QWidget,QMainWindow,QAction,QApplication,qApp,QHBoxLayout,
                             QVBoxLayout,QPushButton)
from PyQt5.QtGui import QPixmap, QIcon

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        #Record Button
        self.rButton = QPushButton(self)
        self.rButton.setToolTip('record')
        rIcon = QPixmap('playIcon.jpeg')
        self.rButton.move(125,50)
        self.rButton.setIcon(QIcon(rIcon))
        self.rButton.clicked.connect(self.rClick)

        #menuBar:saveFile
        saveFile = QAction('&Save', self)
        #saveFile.triggered.connect(qApp.setStateRequest())

        #menuBar: exitAction
        exitAction = QAction('&Exit',self)
        exitAction.triggered.connect(qApp.quit)

        #menuBar
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        #fileMenu.addAction(saveFile)
        fileMenu.addAction(exitAction)
        """
        #Horizontal Widget Layout
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.rButton)

        #Vertical Widget layout
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        """
        #Window Frame
        self.setGeometry(1300,250,350,100)
        self.setWindowTitle("CST 205 Project 2")
        #self.setLayout(vbox)
        self.show()

    #Record click
    def rClick(self):
        print("CLICKED")
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())

"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 1300
        self.top = 250
        self.width = 400
        self.height = 100
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createHorizontalLayout()
 
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
 
        self.show()
 
    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("What is your favorite color?")
        layout = QHBoxLayout()
 
        buttonBlue = QPushButton('Blue', self)
        buttonBlue.clicked.connect(self.on_click)
        layout.addWidget(buttonBlue) 
 
        buttonRed = QPushButton('Red', self)
        buttonRed.clicked.connect(self.on_click)
        layout.addWidget(buttonRed) 
 
        buttonGreen = QPushButton('Green', self)
        buttonGreen.clicked.connect(self.on_click)
        layout.addWidget(buttonGreen) 
 
        self.horizontalGroupBox.setLayout(layout)
 
 
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
"""
