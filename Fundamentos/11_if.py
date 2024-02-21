# Condicional if -> siempre ejecutan operaciones booleanas

if True:
  print("debería ejecutarse")

if False:
  print("Nunca se ejecuta")
  

pet = input("¿Cuál es tu mascota favorita?: \n")

if pet == "perro":
  print("Buen gusto, crack")

elif pet == "gato": # Evalua hasta que sea una con el elif
  print("Los gatos tampoco estan tan mal")
  
elif pet == "pez":
  print("Nice pez")

else:
  print("Que onda, crack")

'''
stock = int(input('Ingrese el numero de stock: \n'))

if stock >= 100 and stock <= 1000:
  print("El stock es correcto")
else: # Si no...
  print("El stock es incorrecto")
'''

# Reto: Saber si el numero es par o impar
numero = int(input("Ingresa un número: \n"))

if (numero % 2) == 0:
  print("Es un número par")

else:
  print("Es un número impar")