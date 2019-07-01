from time import time
from random import choice

farbe = choice(["rot", "gelb", "grün", "blau"])
print("Du bist Spieler mit der Farbe: " + farbe)

print("Bis zu welcher Zahl soll aufaddiert werden?")
zahl = int(input())

i = 0
summe = 0
startTime = time()

while i <= zahl:
   summe = summe + i
   print("summe(" + str(i) + ") = " + str(summe))
   i = i + 1

currentTime = time()
dauer = currentTime - startTime

print("Dauer der Berechnung: " + (str(dauer)) + " Sekunden")