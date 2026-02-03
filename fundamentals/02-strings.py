# Strings en Python

quote = "I'm David" # trabajando con diferentes comillas
print(quote)

nombre = "David"
apellido = "Herrera"

# manipulación del formato
template = "Mi nombre es " + nombre + ", y mi apellido es " + apellido
print(template)

template2 = "Mi nombre es {}, y mi apellido es {}".format(nombre, apellido)
print(template2)

template3 = f"Mi nombre es {nombre}, y mi apellido es {apellido}"
print(template3)

print(nombre[0]) # indexación de caracteres

print(nombre[-0]) # indexación inversa

print(nombre[0:3]) # slicing: primeros 3 caracteres

print (len(nombre)) # longitud

print(nombre * 5) # repetición

print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt") # escape de caracteres