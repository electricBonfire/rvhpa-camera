from PIL import Image 
from PIL import ImageDraw
from PIL import ImageFont

from datetime import datetime

now = datetime.now()
font = ImageFont.truetype("Arial.ttf", 24)
im = Image.open(r"/Users/shawn/Documents/Work/lab/rvhpa/elake.jpg") 
top = 1400
left = 280
im1 = im.crop((left,top,left + 3000,top + 800))
im1 = im1.resize((1500, 400))
draw = ImageDraw.Draw(im1)
draw.rectangle((600,0,1020,24), fill="#ffffff")
draw.text((600,0), "ELAKE - Bottom Sock - " + now.strftime("%d/%m/%y %H:%M"), (0,0,0), font)
im1.save('/Users/shawn/Documents/Work/lab/rvhpa/test-crop.jpg')