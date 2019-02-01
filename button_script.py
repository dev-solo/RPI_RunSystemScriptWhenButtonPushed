import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23

try:
    while True:
         button_state = GPIO.input(23)
         if button_state == False:
             print('Button Is Pressed...')
             os.system("~/camera/camera.sh")
             time.sleep(0.5)
except:
    GPIO.cleanup()
