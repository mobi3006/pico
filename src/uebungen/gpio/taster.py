from RPi import GPIO
import time

# GPIO initialisieren
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(8, GPIO.IN)

count = 0

while True:
   # Spannungspotential aufbauen (verbunden mit +3,3V) => Strom fliessen lassen
   GPIO.output(37, False)
   start = time.time
   print("start: " + start)
   stop = False
   while not stop:
      taster = GPIO.input(8)
      if taster:
         count = count + 1
      currentTime = time.time
      print("currentTime: " + currentTime)
      stop = (currentTime - start) > 10

GPIO.cleanup
