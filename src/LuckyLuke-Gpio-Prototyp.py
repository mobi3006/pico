# ACHTUNG: dieser Code funktioniert nur mit der entsprechenden Verkabelung auf dem RPi-GPIO

import RPi.GPIO as GPIO
import time
from time import clock
from time import localtime

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
input_pin = 37
GPIO.setup(38,GPIO.OUT)
GPIO.setup(input_pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def ledAn():
    GPIO.output(38,True)

def ledAus():
    GPIO.output(38,False)

punktzahl = 0
spielBeginn = time.time()
while (time.time() - spielBeginn < 30.0 ):
    
        ledAn()

        startDurchgang = time.time()
        while (time.time() - startDurchgang < 3.0):
            istTasteJetztGedrueckt = GPIO.input(input_pin)
            if (istTasteJetztGedrueckt):
                punktzahl = punktzahl + 1
                print("Treffer - aktuelle Punktzahl: " + str(punktzahl))
                break

        print("Runde ist rum ... nächste Runde")
        ledAus()

        time.sleep(0.2)

print("Ergebnis: " + str(punktzahl))