# Juego de piedra, papel o tijera
import random

opciones = ('piedra', 'papel', 'tijera')

ronda = 1
userWins = 0
compWins = 0

while True:
  print('***' * 10)
  print('Ronda:', ronda)
  print('Victorias del usuario:', userWins)
  print('Victorias de la computadora:', compWins)

  userOp = input("¿Piedra, papel o tijera? ").lower()
  compOp = random.choice(opciones) # Escoge algo basado en una tupla/lista

  if userOp not in opciones: # Si no eliges una opción valida
    print('No es una opción valida')
    continue

  print('Opción de la computadora: ', compOp)

  if userOp == compOp:
    print("Es un empate")

  elif userOp == "piedra":
    if compOp == "tijera":
      print("Ganaste")
      userWins += 1
    else:
      print("Perdiste")
      compWins += 1

  elif userOp == "papel":
    if compOp == "tijera":
      print("Perdiste")
      compWins += 1
    else:
      print("Ganaste")
      userWins += 1

  elif userOp == "tijera":
    if compOp == "piedra":
      print("Perdiste")
      compWins += 1
    else:
      print("Ganaste")
      userWins += 1

  if compWins == 2:
    print("Computadora gana!!!")
    break

  elif userWins == 2:
    print("Usuario gana!!!")
    break

  else:
    ronda += 1
