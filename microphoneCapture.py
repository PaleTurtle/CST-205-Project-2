filename=input('Please enter the filename you want:')
starttime=input('When do you want to start?')
time=input('How long do you want to record?')
def callCommand(command):
    subprocess.Popen(command.split(' '))
    
callCommand('ffmpeg -f alsa -ac 2 -ar 44100 -ss {} -t {} -i hw:0,1 {}.wav'.format(starttime,time,filename))
