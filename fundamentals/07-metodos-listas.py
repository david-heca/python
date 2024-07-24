# Métodos de las listas en Python
# CRUD: Create, Read, Update, Delete

numbers = [1,2,3,4,5] # Create
print(numbers[2]) # Read
numbers[-1] = 10 # Update
print(numbers)

numbers.append(700) # agregar un nuevo elemento al final de la lista
print(numbers)

numbers.insert(4, 900) # insert recibe la posición y el elemento nuevo para insertar
print(numbers)

tareas = ['todo1','todo2','todo3']
nueva = tareas + numbers # unir/concatenar listas
print(nueva)

print(nueva.index('todo2')) # nos devuelve la posición de un elemento en la lista

# Delete

nueva.remove('todo3') # remueve un elemento en especifico
print(nueva)

# print(nueva.pop()) # elimina el ultimo elemento de una lista y lo devuelve
print(nueva.pop(0)) # elimina un elemento en especifico

nueva.reverse() # Muestra la lista al reves
print(nueva)

numbers.sort() # ordena la lista del menor al mayor
print(numbers)

# Slice en Python

a = [1,2,3,4,5]
b = a #b apuntara al mismo espacio de memoria que a
print(a)
print(b)

del a[0] # elimina un elemento de la lista
print(a)
print(b)
print(id(a), id(b))

c = a[:] # c apuntara a un nuevo espacio de memoria
print(c)
print(id(a), id(c))