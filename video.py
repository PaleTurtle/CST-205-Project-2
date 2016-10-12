from PIL import ImageGrab
from PIL import Image
from ffmpy import FFmpeg

Image_VideoList = []

for x in range(1,5):
    ImageGrab.grab().save((str(x)) + "screenshot.jpg", "JPEG")

for imageNumber in range(1,5):
    Image_VideoList.append((str(imageNumber)) + "screenshot.jpg")

# print (Image_VideoList)

video = FFmpeg(
        inputs={'input.ts' = ImageVideoList,
        outputs ={'output.mp4':
