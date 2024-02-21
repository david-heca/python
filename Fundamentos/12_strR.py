# Strings recargados en python

text = 'Ella sabe programar en Python'
print('JavaScript' in text) # Busca si el texto que añadimos esta en la variable
print('Python' in text) # Devuelve True o False

if 'Python' in text:
  print('Que buena lectura')

else:
  print('Deberías aprender Pyhton')

# METODOS DE STRINGS

size = len(text) # Metodo que examina el tamaño de caracteres (contando espacios)
print(size)

print(text.upper()) # Convierte el texto a mayusculas
print(text.lower()) # Minusculas
print(text.count('a')) # Cuantas veces hay una 'a'
print(text.swapcase()) # Hace swap en cuanto a las mayus y minus
print(text.startswith('Ella')) # Identifica si empieza con... (devuelve bool)
print(text.replace('Python', 'Go')) # Reemplazar un texto

text2 = '  este es un titulo   '

print(text2.capitalize()) # Formato de texto capitalize
print(text2.title()) # Cada palabra tiene mayus
print(text2.isdigit()) # Si es un digito
print(text2.strip()) # Quita espacios al inicio y final

# https://www.w3schools.com/python/python_strings_methods.asp