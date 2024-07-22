# Condicional if en Python -> siempre ejecutan operaciones booleanas

if True:
  print("debería ejecutarse")

if False:
  print("Nunca se ejecuta")

# Ejemplo de un if almacenando un valor
pet = input("¿Cuál es tu mascota favorita?: \n")

if pet == "perro":
  print("Buen gusto, crack")
elif pet == "gato": # Evalua hasta que sea una con el elif
  print("Los gatos tampoco estan tan mal")
elif pet == "pez":
  print("Nice pez")
else:
  print("Que onda, crack")

# Reto: Saber si el numero es par o impar
numero = int(input("Ingresa un número: \n"))

if (numero % 2) == 0:
  print("Es un número par")
else:
  print("Es un número impar")