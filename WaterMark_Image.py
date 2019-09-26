"""

Python script to time stamp images

Created by : Praphul 

Date : 25/09/2018

"""


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import glob, re , os

files = sorted(glob.glob1(os.getcwd(),'*.bmp'))

t = 100

for j in files: 
     photo = Image.open(os.getcwd()+"/"+j)
     drawing = ImageDraw.Draw(photo)

     font = ImageFont.truetype("Pillow/Tests/fonts/FreeMonoBold.ttf",16)
     pos = (0.2,0.65)

     red = (255, 0, 0)

     text = 'TIME - ' + str(t) + ' s'

     drawing.text(pos,text, fill=red, font=font)
     
     if os.path.isdir(os.getcwd()+"/timeStampImgs") == False:
         print("Creating new directory for time stamp images")
         os.mkdir(os.getcwd()+"/timeStampImgs")

     photo.save(os.getcwd()+"/timeStampImgs/"+str(t)+'.bmp')

      
     t = t + 5
