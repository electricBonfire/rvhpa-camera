from time import sleep
from picamera import PiCamera, Color
from ftplib import FTP
import os
from datetime import datetime
from PIL import Image 
from PIL import ImageDraw
from PIL import ImageFont

try:
    upload_ftp = os.getenv('RVHPA_FTP_URL')
    upload_user = os.getenv('RVHPA_FTP_USER')
    upload_password = os.getenv('RVHPA_FTP_PASS')
except:
    raise Exception('Environmental variables with FTP info cannot be loaded')

ftp = FTP(upload_ftp, upload_user, upload_password)

try:
    camera = PiCamera()
    camera.resolution = (3280, 2464)
    camera.start_preview()
    # camera.annotate_text = "  Elake  "
    # camera.annotate_background = Color('#f12362')
    # sleep(2)
    camera.zoom = (0,0,0,0)
    camera.capture('/tmp/elake.jpg')
finally:
    camera.close()

try:
  img = Image.open('/tmp/elake.jpg')
  now = datetime.now()
  font = ImageFont.truetype("Arial.ttf", 24)
  draw = ImageDraw.Draw(img)
  draw.rectangle((0,0,420,24), fill="#ffffff")
  draw.text((0,0), "ELAKE - Bottom Sock - " + now.strftime("%d/%m/%y %H:%M"), (0,0,0), font)
  img.save('/tmp/elake-1.jpg')
  
  ftp.storbinary('STOR /elake/elake-temp.jpg', img)
  ftp.rename('/elake/elake-temp.jpg', '/elake/elake.jpg')

except e:
    print('Exception: %s' % (e,))
    try:
        ftp.close()
        # ftp = FTP(upload_ftp, upload_user, upload_password)
    except f:
        print('Error, %s and %s' % (e, f))
#time.sleep(300)