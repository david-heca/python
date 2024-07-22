# Variables en Python

# Python es un lenguaje ordenado y limpio, va de arriva hacía abajo y de izquierda a derecha
# Las variables son contenedores de información

nombre = "David"
print(type(nombre)) # str

edad = 23
print(type(edad)) # int

soltero = True
print(type(soltero)) # bool

nombre = "Aaron" # sobreescritura de una variable
print("Mi nombre es: " + nombre) # concatenación

# Input o entrada de datos

nombre = input("¿Cuál es tu nombre? \n")
print("Tu nombre es:", nombre, "y su tipo de dato es:", type(nombre)) # la coma agrega un espacio