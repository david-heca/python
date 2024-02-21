# Ciclos: WHILE en Python

'''
while True: # Mientras sea True
  print('Se ejecuto')


contador = 0
while contador < 10:
  contador += 1 # Cada vez que se ejecute se suma uno
  print(contador)


contador = 0
while contador < 20:
  contador +=1
  if contador == 15:
    break # Forma forzada de romper el ciclo
  print(contador)
'''

contador = 0
while contador < 20:
  contador += 1
  if contador <= 15:
    continue # Salta la logica posterior al continue y vuelve a iterar
  print(contador)