# Listas/Arrays en Python

to_do = ['Ir al hotel',
         'Ir a almorzar',
         'Visitar un museo',
         'Regresar al hotel'] # las listas permiten almacenar varios valores
print(to_do)

numbers = [1,2,3,4,5]
print(type(numbers))

tareas = ['lavar', 'jugar', 'limpiar'] # tienen un orden definido
print(tareas)

Tipos = [True, 12, 'Rojo', '😁', [1, 2, 3]] # puede almacenar todo tipo de datos

print(numbers[2]) # indexing: acceder a un elemento de la lista

text = 'Hola'
tareas[2] = text # modificar un elemento de la lista
print(tareas)

print(numbers[1:3]) # slicing: obtener un rango de elementos de la lista

print(True in Tipos) # verificar si un elemento está en la lista
