"""
Title: Screen Recorder
Authors: Sean Trehy, Julia Werner, Victor Done
Course: CST 205
Due Date: 10/14/2016
Abstract: This program will record the screen and capture audio from the microphone.
GUI: Sean
Audio: Julia
Video:Victor
GitHub link: https://github.com/PaleTurtle/CST-205-Project-2
"""

import sys
import subprocess
import os.path as pt
import pyscreenshot as ImageGrab
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
        self.rButton.move(105,50)
        self.rButton.setIcon(QIcon(rIcon))
        self.rButton.clicked.connect(self.rClick)

        #File: saveFile
        saveFile = QAction('&Save File',self)
        saveFile.setShortcut('Ctrl+s')
        saveFile.setStatusTip('Save recording')
        saveFile.triggered.connect(self.save_file)

        #File: exitAction
        exitAction = QAction('&Exit',self)
        exitAction.setShortcut('Ctrl+q')
        exitAction.triggered.connect(qApp.quit)

        #menuBar
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        
        #menuBar: File
        fileMenu.addAction(saveFile)
        #fileMenu.addAction(saveAs)
        fileMenu.addAction(exitAction)
        
        #Window Frame
        self.setGeometry(1300,250,325,100)
        self.setWindowTitle("Screen Recorder")
        self.show()

    #save_file
    def save_file(self):
        saveName = QtGui.QFileDialog.getSaveFileName(self, 'Save File', 'c:\\')
        file = open(saveName, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()
        
    #Record click
    def rClick(self):
        filename="newfile"
        counter=0
        time=20
        filenumber=1

        while(pt.exists(filename+str(filenumber)+".mp4")):
            filenumber+=1

        for x in range(1,10):
                counter = counter + 1   
                if(counter<=10):
                        ImageGrab.grab().save("screenshot00"+(str(x))+".png")
                elif(counter>10 and counter<=100):
                        ImageGrab.grab().save("screenshot0"+(str(x))+".png")
                elif(counter>100 and counter<1000):
                        ImageGrab.grab().save("screenshot"+(str(x))+".png")

        subprocess.call('ffmpeg -framerate 1/5 -f image2 -i screenshot%03d.png -c:v libx264 -vf fps=1 fvideo.ts', shell="TRUE")
        
        def callCommand(command):
            #open the command in the subprocess and split it into the parts that should be executed
            subprocess.Popen(command.split(' '))

        #use the command for the FFmpeg function
        callCommand('ffmpeg -f alsa -ac 2 -ar 44100 -ss 00:00:00 -t 20 -i hw:0,1 project2finaltest.mp3')
        callCommand('ffmpeg -i fvideo.ts -i project2finaltest.mp3 -c:v copy -c:a copy {}{}.mp4'.format(filename,filenumber))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())