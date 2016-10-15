from PIL import ImageGrab #Allows us to use ImageGrab = Screenshot

import subprocess

#run screenshots
counter = 0
for x in range(1,time
):
	counter = counter + 1
	if(counter<=10):
		ImageGrab.grab().save("screenshot00" + str(x) + ".png")
	elif(counter>10 and counter<100):
		ImageGrab.grab().save("screenshot0" + str(x) + ".png")
	elif(counter>=100 and counter<1000):
		ImageGrab.grab().save("screenshot" + str(x) + ".png")
	


#convert to video using ffmpeg
subprocess.call('ffmpeg -r 1 -f image2 -i /Desktop/Project205/screenshot%03d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p ssvideo.ts')

# to combine audio and video using ffmpeg
# ffmpeg -i (video file) -i (audio file) -c:v copy -c:a copy (outputname).mp4))
