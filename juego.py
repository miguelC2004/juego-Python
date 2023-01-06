import random

adivinanza = random.randint(1, 10)

while True:
  intento = int(input("Adivina el número (1 a 10): "))
  if intento == adivinanza:
    print("¡Felicidades, has adivinado el número!")
    break
  else:
    print("Lo siento, ese no es el número. Inténtalo de nuevo.")
