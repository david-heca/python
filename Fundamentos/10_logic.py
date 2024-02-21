# Operadores logicos

# AND, las dos tienen que dar verdadero
print('True and True =>', True and True) # True
print('True and False =>', True and False) # False
print('False and True =>', False and True) # False
print('False and False =>', False and False) # False

# Ejemplos con números
print(10 > 5 and 5 < 10) # True
print(10 > 5 and 5 > 10) # False

# Verificar el inventario de una empresa
stock = int(input('Ingrese el numero de stock: \n'))
# Establece limites de minimo y maximo
print(stock >= 100 and stock <= 1000)

# OR, solo con uno sea verdadero
print('True or True =>', True or True) # True
print('True or False =>', True or False) # True
print('False or True =>', False or True) # True
print('False or False =>', False or False) # False

role = input('Digaita el rol: \n')
print(role == 'admin' or role == 'seller') # admin o vendedor, solo en ese caso True

# NOT, este niega una condición y cambia el inverso del booleano
print(not True)
print(not False)

print('True and True =>', not (True and True)) # False
print('True and False =>', not (True and False)) # True
print('False and True =>', not (False and True)) # True
print('False and False =>', not (False and False)) # True

# Negación del ejercicio and, todo el rango de 100 y 1000 da False
stock = int(input('Ingrese el numero de stock: \n'))
print(not(stock >= 100 and stock <= 1000))