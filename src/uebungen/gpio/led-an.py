from RPi import GPIO

# GPIO initialisieren
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)

while True:
   print("an oder aus?")
   state = input()
   if state == "an":
      # Spannungspotential aufbauen (verbunden mit +3,3V) => Strom fliessen lassen
      GPIO.output(37, False)
   else:
      GPIO.output(37, True)

GPIO.cleanup
