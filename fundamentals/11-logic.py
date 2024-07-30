# Operadores logicos en Python

# AND, las dos tienen que dar True
print('True and True =>', True and True) # True
print('True and False =>', True and False) # False
print('False and True =>', False and True) # False
print('False and False =>', False and False) # False

# Ejemplos con números
print(10 > 5 and 5 < 10) # True
print(10 > 5 and 5 > 10) # False

# OR, solo uno tiene que dar True
print('True or True =>', True or True) # True
print('True or False =>', True or False) # True
print('False or True =>', False or True) # True
print('False or False =>', False or False) # False

# NOT, este niega una condición y devuelve el valor contrario
print(not True)
print(not False)

print('not True and True =>', not (True and True)) # False
print('not True and False =>', not (True and False)) # True
print('not False and True =>', not (False and True)) # True
print('not False and False =>', not (False and False)) # True