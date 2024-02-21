# Métodos de las listas en Python
# CRUD: Create, Read, Update, Delete

numbers = [1,2,3,4,5] # Create
print(numbers[2]) # Read
numbers[-1] = 10 # Update
print(numbers)

numbers.append(700) # Podemos agregar un nuevo elemento al final de la lista
print(numbers)

numbers.insert(4, 900) # insert recibe la posición y el elemento nuevo para insertar
print(numbers)

tareas = ['todo1','todo2','todo3']
nueva = tareas + numbers # Podemos unir/concatenar listas
print(nueva)

print(nueva.index('todo2')) # Saber la posición de un elemento en especifico

# Delete

nueva.remove('todo3') # Remueve un elemento en especifico
print(nueva)

# print(nueva.pop()) # Elimina el ultimo elemento de una lista y lo devuelve
print(nueva.pop(0)) # También puedes elegir una posición

nueva.reverse() # Muestra la lista al reves
print(nueva) 

numbers.sort() # Ordena la lista del menor al mayor (también en Stings)
print(numbers) # No ordena datos mezclados