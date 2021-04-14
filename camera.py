import picamera
from time import sleep
camera=picamera.PiCamera()
camera.vflip=None
camera.start_preview(fullscreen=True)
sleep(30)
camera.start_preview()