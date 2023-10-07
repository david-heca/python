# Conjuntos/Sets en Python

# Los sets no tienen par key-value, solo tienen valores
set_countries = {'mex', 'col', 'bol'}
print(type(set_countries))

# Un conjunto puede tener diferentes tipos, pero no se pueden repetir los elementos
set_types = {1, 'hola', False, 12.4, 'hola'}
print(set_types)

set_from_string = set('holaaa') # Crea un conjunto a partir de la palabra 'Hola'
print(set_from_string) # Al imprimir se eliminan elementos duplicados

set_from_tuples = set(('abc', 'cbv', 'as')) # Conjunto de una tupla

numbers = [1,2,3,1,2,3,4]
set_numbers= set(numbers) # Cremos un conjunto a partir de una lista

unique_numbers = list(set_numbers) # Podemos convertir un conjunto a una lista
print(unique_numbers) 
