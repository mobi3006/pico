from RPi import GPIO
import time

# GPIO initialisieren
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)

state = "an"
while True:
   if state == "an":
      # Spannungspotential aufbauen (verbunden mit +3,3V) => Strom fliessen lassen
      GPIO.output(37, False)
      state = "aus"
   else:
      GPIO.output(37, True)
      state = "an"
   time.sleep(0.1)

GPIO.cleanup
