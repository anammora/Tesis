import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
def run():
    servoPIN = 22
    
    GPIO.setup(servoPIN, GPIO.OUT)
    
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(5) # Initialization
    time.sleep(1)
    p.ChangeDutyCycle(10)
    time.sleep(1)
    p.stop()
    #GPIO.cleanup()
#run()
#p.ChangeDutyCycle(7.5)
#time.sleep(1)

'''
try:
  while True:
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
'''