import os.path as pt
import subprocess
#import the subprocess for oprations with FFmpeg and the command line
#link to GitHub: https://github.com/PaleTurtle/CST-205-Project-2/
#filename is created:
#create filename string and a filenumber
filename="newfile"
filenumber=1
#got some help from stackoverflow: https://stackoverflow.com/questions/17984809/how-do-i-create-an-incrementing-filename-in-python
#as long as the filename in combination with the filenumber alreadz exists, the filenumber is increased
while(pt.exists(filename+str(filenumber)+".mp3")):
    filenumber+=1
#user chooses the amount of time he wants to record
time=input('How long do you want to record(seconds)?')
#callCommand function:call the FFmpeg command in python, even though it is made for command line
#got some help from stackoverflow:https://stackoverflow.com/questions/7656308/python-ffmpeg-command-line-issues
#input: the FFmpeg command
def callCommand(command):
    #open the command in the subprocess and split it into the parts that should be executed
    subprocess.Popen(command.split(' '))

#use the command for the FFmpeg function
callCommand('ffmpeg -f alsa -ac 2 -ar 44100 -ss 00:00:00 -t {} -i hw:0,1 {}{}.mp3'.format(time,filename,filenumber))
            #'ffmpeg: execute FFmpeg
            #-f alsa:format of capturing is ALSA
            #-ac 2:2 audio channels: stereo recording
            #-ar 44100: audio rate: 44100 Hz (usual rate for audio recording) 
            #-ss 00:00:00: start from the beginning
            #-t 20: record for 20 seconds
            #-i: input: all the stuff from before is used as input
            #hw:0,1: select channel for microphone
            #{}{}.mp3': filename string and filenumber are used for the output file
            #.format(filename,filenumber):filename and filenumber are used to fill the gaps in command
