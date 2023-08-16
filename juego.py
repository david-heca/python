# Juego de piedra, papel o tijera

import random

opciones = ('piedra', 'papel', 'tijera')


def elegirOpciones():
    userOp = input("¿Piedra, papel o tijera? ").lower()
    compOp = random.choice(opciones) # Escoge una opción random

    if userOp not in opciones: # Si no eliges una opción valida
        print('No es una opción valida')
        return None, None

    print('Opción de la computadora: ', compOp)

    return userOp, compOp

def reglas(userOp, compOp, userWins, compWins):
    
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

    return userWins, compWins

def resultado(userWins, compWins, ronda):
    if compWins == 2:
        print("Computadora gana!!!")

    elif userWins == 2:
        print("Usuario gana!!!")

    else:
        ronda += 1

    return userWins, compWins, ronda

def runGame():
    userWins = 0
    compWins = 0
    ronda = 1

    while True:
        print('****' * 10)
        print('Ronda:', ronda)
        print('Victorias del usuario:', userWins)
        print('Victorias de la computadora:', compWins)

        userOp, compOp = elegirOpciones()

        if userOp != None:
            userWins, compWins = reglas(userOp, compOp, userWins, compWins)
            
            userWins, compWins, ronda =  resultado(userWins, compWins, ronda)
            if userWins == 2 or compWins == 2:
                break

runGame()
