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
        
        #import the subprocess for oprations with FFmpeg and the command line
        #link to GitHub: https://github.com/PaleTurtle/CST-205-Project-2/
        #user chooses the filename for the output file
        filename=input('Please enter the filename you want:')
        #user chooses the amount of time he wants to record
        time=input('How long do you want to record(seconds)?')
        #callCommand function:call the FFmpeg command in python, even though it is made for command line
        #got some help from stackoverflow:https://stackoverflow.com/questions/7656308/python-ffmpeg-command-line-issues
        #input: the FFmpeg command
        def callCommand(command):
            #open the command in the subprocess and split it into the parts that should be executed
            subprocess.Popen(command.split(' '))

        #use the command for the FFmpeg function
        callCommand('ffmpeg -f alsa -ac 2 -ar 44100 -ss 00:00:00 -t {} -i hw:0,1 {}.wav'.format(time,filename))
            #'ffmpeg: execute FFmpeg
            #-f alsa:format of capturing is ALSA
            #-ac 2:2 audio channels: stereo recording
            #-ar 44100: audio rate: 44100 Hz (usual rate for audio recording) 
            #-ss 00:00:00: start from the beginning
            #-t {}: record for the time the user entered
            #-i: input: all the stuff from before is used as input
            #hw:0,1: select channel for microphone
            #{}.wav': filename the user entered is used for the output file
            #.format(time,filename)):input from user is used to fill the gaps in command
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())

