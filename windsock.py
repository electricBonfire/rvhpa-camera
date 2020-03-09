from time import sleep
from picamera import PiCamera, Color
from ftplib import FTP
import os

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
    camera.annotate_text = "  Elake  "
    camera.annotate_background = Color('#f12362')
    sleep(2)
    camera.zoom = (0.35,0.35,0.65,0.65)
    camera.capture('/tmp/elake.jpg')
finally:
    camera.close()

try:
  f = open('/tmp/elake.jpg', 'rb')
  ftp.storbinary('STOR /elake/elake-temp.jpg', f)
  ftp.rename('/elake/elake-temp.jpg', '/elake/elake.jpg')

except e:
    print('Exception: %s' % (e,))
    try:
        ftp.close()
        ftp = FTP(upload_ftp, upload_user, upload_password)
    except f:
        print('Error, %s and %s' % (e, f))
#time.sleep(300)