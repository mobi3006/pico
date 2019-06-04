import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
input_pin = 37


GPIO.setup(38,GPIO.OUT)
GPIO.setup(input_pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
zustand = False

while True:
    if (GPIO.input(input_pin) == True):
        if (zustand == True):
            zustand = False
        else:
            zustand = True
        GPIO.output(38,zustand)
        
        time.sleep(0.5)
        
GPIO.cleanup()