from PIL import Image 
from PIL import ImageDraw
from PIL import ImageFont

from datetime import datetime

now = datetime.now()
font = ImageFont.truetype("Arial.ttf", 24)
im = Image.open(r"/Users/shawn/Documents/Work/lab/rvhpa/test.jpg") 
im1 = im.crop((0,0,600,400))
draw = ImageDraw.Draw(im1)
draw.rectangle((0,0,420,24), fill="#ffffff")
draw.text((0,0), "ELAKE - Bottom Sock - " + now.strftime("%d/%m/%y %H:%M"), (0,0,0), font)
im1.save('/Users/shawn/Documents/Work/lab/rvhpa/test-crop.jpg')