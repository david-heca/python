# Indexing y Slicing en Pyhton

# Indexing
text = 'Ella sabe Python'
print(text[0]) # Accedemos a la posición 0 de la variable
print(text[12])

print(text[len(text)-1]) # Conocer la ultima posición
print(text[-1]) # Otra manera de conocerla

# Slicing
print(text[0:5]) # Obteniendo una parte del texto
print(text[10:16])
print(text[:10]) # Si no envias nada al incio inicia en 0 y visceversa
print(text[5:])