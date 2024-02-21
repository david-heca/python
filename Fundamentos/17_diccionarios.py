# Diccionarios en Python

dicc = {
  'nombre': 'david',
  'apellido': 'herrera',
  'edad': 22
}

print(type(dicc)) # Verificamos el tipo
print(len(dicc)) # Conocer el numero de elementos
print(dicc) 
print(dicc['edad']) # Podemos obtener un valor de la key

# Una manera de trabajar sin dejar de compilar en caso de error, obtenemos un valor o no
print(dicc.get('edad2')) 

print('edad' in dicc) # Verificamos que esta en el dicc

# Inserción y actualización
dicc2 = {
  'nombre': 'david',
  'apellido': 'herrera',
  'lenguajes': ['Pyhton', 'JS'], # Puede haber arreglos como atributos del diccionario
  'edad': 22
}

dicc2['nombre'] = 'aaron' # Podemos cambiar un valor
dicc2['edad'] -= 2 # Y restar valores numericos directamente
dicc2['lenguajes'].append('Rust') # Podemos trabajar con la lista dentro del dicc
print(dicc2)

del dicc2['apellido'] # Si queremos eliminar un atributo
# dicc2.pop('edad') # Tambien eliminar con POP
print(dicc2)

print('items *****') # Devuelve tuplas de cada elemento del diccionario
print(dicc2.items())

print('keys *****') # Devuelce una tupla con los keys
print(dicc2.keys())

print('values *****') # Devuelve directamente los valores
print(list(dicc2.values())) # Podemos imprimir solo como lista