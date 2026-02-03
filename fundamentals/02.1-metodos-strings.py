# Métodos de strings en Python

espacios = "   Hola Mundo   "
print(espacios.strip()) # eliminar espacios en blanco al inicio y final
print(espacios.lstrip()) # eliminar espacios en blanco al inicio
print(espacios.rstrip()) # eliminar espacios en blanco al final
print(espacios.replace("Mundo", "Python")) # reemplazar texto

print(espacios.lower()) # convertir a minúsculas
print(espacios.upper()) # convertir a mayúsculas
print(espacios.capitalize()) # primera letra en mayúscula
print(espacios.title()) # primera letra de cada palabra en mayúscula    
print(espacios.count("o")) # contar ocurrencias de un carácter o subcadena
print(espacios.find("Mundo")) # encontrar la posición de una subcadena