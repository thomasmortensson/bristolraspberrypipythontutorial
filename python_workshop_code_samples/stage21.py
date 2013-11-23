''' GPIO - Example ''' 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, 0)
test = False
while True:
        if(test):
                GPIO.output(16,1)
                test = False
                time.sleep(1)
        else:
                GPIO.output(16,0)
                test = True
                time.sleep(1)